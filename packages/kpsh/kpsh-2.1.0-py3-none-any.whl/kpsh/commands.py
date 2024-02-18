# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2019 Michał Góral.

import os
import argparse
import subprocess
import time
import fnmatch
import shlex
import string
import secrets
import collections
import contextlib
from copy import deepcopy

from kpsh import threads
from kpsh.environment import detect_environment, OS, Environment
from kpsh.clipboard import copy_to_clipboard, clear_clipboard
from kpsh.cleanup import cleanup
from kpsh.entry import EntryProxy


class CommandError(Exception):
    pass


class ArgumentParserError(Exception):
    pass


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


class reraise_as:
    def __init__(self, eout, msg="{}", eins=None):
        self.eout = eout
        self.msg = msg

        if eins is None or isinstance(eins, (list, tuple)):
            self.eins = eins
        else:
            self.eins = [eins]

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type and (not self.eins or exc_type in self.eins):
            s = str(exc_val).strip("'\"")
            raise self.eout(self.msg.format(s))
        return False


@contextlib.contextmanager
def stop_on_error(revert_fn, *args, **kwargs):
    try:
        yield
    except:
        if revert_fn:
            revert_fn(*args, **kwargs)
        raise


def prepare_command_parser():
    cp = ThrowingArgumentParser(prog="", add_help=False)
    sp = cp.add_subparsers(required=True)

    parsers = {}
    parsers[None] = cp

    # helper function which automatically creates help-friendly parsers
    def add_parser(command, *a, **kw):
        kw["add_help"] = False

        descr = kw.get("description")
        if descr:
            kw["description"] = "{}\n\n{}".format(kw["help"], descr)
        else:
            kw["description"] = kw["help"]

        parser = sp.add_parser(command, *a, **kw)
        parsers[command] = parser
        return parser

    ######### open
    open_sp = add_parser(
        "open",
        help="Change currently opened database. New database will be created if it doesn't exist.",
    )
    open_sp.add_argument("filepath", help="path to database file.")
    open_sp.set_defaults(func=open_)

    ######### unlock
    unlock_sp = add_parser("unlock", help="Unlock currently opened database.")
    unlock_sp.add_argument(
        "--keyfile", default="", help="key file used for unlocking database"
    )
    unlock_sp.set_defaults(func=unlock)

    ######### lock
    lock_sp = add_parser("lock", help="Lock current database.")
    lock_sp.set_defaults(func=lock)

    ######### db
    db_sp = add_parser("db", help="Query opened database info.")
    db_sp.set_defaults(func=db)

    ######### ls
    ls_sp = add_parser("ls", help="List contents of database.")
    ls_sp.add_argument(
        "glob",
        nargs="?",
        default="*",
        help="display only entries which match glob expression",
    )
    ls_sp.set_defaults(func=ls)

    ######### show
    show_sp = add_parser(
        "show", help="Show contents of entry.", description="Search is case-sensitive."
    )
    show_sp.add_argument("path", help="path which should be shown")
    show_sp.add_argument("fields", nargs="*", help="only display certain fields")
    show_sp.add_argument(
        "-n",
        "--no-field-name",
        action="store_true",
        help="hide field names in the output",
    )
    show_sp.set_defaults(func=show)

    ######### add/edit
    add_sp = add_parser(
        "add",
        help="Add a new entry if it doesn't exist yet.",
        description="New entry can be in form 'group/name'. In that case, "
        "it will be added as a member of existing group or the new "
        "group will be created",
    )
    edit_sp = add_parser("edit", help="Edit existing entry")

    for spr in (add_sp, edit_sp):
        spr.add_argument("path", help="entry path")
        spr.add_argument("-u", "--username", help="username")
        spr.add_argument("-p", "--password", help="password")

        if spr is edit_sp:
            spr.add_argument(
                "--askpass",
                action="store_true",
                help="interactively ask for password; input will be hidden",
            )

        spr.add_argument("-U", "--url", help="URL")
        spr.add_argument(
            "-n",
            "--note",
            action="append",
            dest="notes",
            help="add a line in notes. Many notes can be added "
            "by using -n more than once. New notes are added after deletion "
            "of the old ones.",
        )

        if spr is edit_sp:
            spr.add_argument(
                "-N",
                "--delete-note",
                dest="delnotes",
                metavar="NOTES",
                help="delete note. Notes are accessed by their index. Range of "
                "notes can be deleted by passing e.g. '-N 2-5', or all notes can "
                "be deleted by passing '-N *'",
            )

        spr.add_argument(
            "-s",
            "--autotype-sequence",
            metavar="KEYS",
            help="key sequence used for autotyping",
        )

        property_help = "set custom property named PROPERTY to the value VALUE."
        if spr is edit_sp:
            property_help += " If PROPERTY is empty ('property='), it will be"
            property_help += " deleted."
        property_help += " Spaces around name and value are preserved, so"
        property_help += " 'name=val' and 'name = val' are different entries."
        spr.add_argument(
            "-t",
            "--property",
            action="append",
            dest="properties",
            metavar="PROPERTY=VALUE",
            help=property_help,
        )

        sp_gen = spr.add_argument_group("password generation")
        sp_gen.add_argument(
            "-g",
            "--generate-password",
            dest="pw_gen",
            action="store_const",
            const="interactive",
            help="enable interactive password generation if --password is not "
            "set. By default password is generated from ASCII letters and "
            "digits. New password must be accepted before it is saved",
        )
        sp_gen.add_argument(
            "-G",
            "--generate-password-no-confirm",
            dest="pw_gen",
            action="store_const",
            const="noninteractive",
            help="same as --generate-password, but kpsh will automatically"
            "save generated password, without any user confirmation",
        )
        sp_gen.add_argument(
            "--letters",
            dest="charset",
            action="append_const",
            const=string.ascii_letters,
            help="use ASCII letters in generated password: a-z, A-Z",
        )
        sp_gen.add_argument(
            "--digits",
            dest="charset",
            action="append_const",
            const=string.digits,
            help="use digits in generated password: 0-9",
        )
        sp_gen.add_argument(
            "--logograms",
            dest="charset",
            action="append_const",
            const="#$%&@^`~",
            help="use logograms in generated password: #$%%&@^`~",
        )
        sp_gen.add_argument(
            "--punctuation",
            dest="charset",
            action="append_const",
            const=string.punctuation,
            help=f"use punctuation symbols in generated password: !#,.:; etc.",
        )
        sp_gen.add_argument(
            "--characters",
            help="characters which should be used for password generation. "
            "Setting this option overrides usage of --letters, --digits and "
            "--punctuation.",
        )
        sp_gen.add_argument(
            "-l",
            "--length",
            metavar="N",
            type=int,
            default=20,
            help="length of generated password (default: 20)",
        )

    add_sp.set_defaults(func=add)
    edit_sp.set_defaults(func=edit)

    ######### delete
    del_sp = add_parser("delete", help="Delete entry from database")
    del_sp.add_argument("paths", nargs="+", help="path of entry to remove")
    del_sp.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="delete groups and their contents recursively.",
    )
    del_sp.set_defaults(func=delete)

    ######### move
    del_sp = add_parser("move", help="Move entry to the new path.")
    del_sp.add_argument("source", help="path to be moved")
    del_sp.add_argument("dest", help="new path")
    del_sp.set_defaults(func=move)

    ######### copy
    cp_sp = add_parser("clipboard", help="Copy username or password to the system clipboard")
    cp_sp.add_argument("path", help="path from which fields should be copied")
    cp_sp.add_argument(
        "field", help="select a field to copy", choices=("username", "password")
    )
    cp_sp.add_argument(
        "-c",
        "--clear-after",
        default=10,
        type=int,
        help="seconds after which clipboard will be cleared",
    )
    cp_sp.add_argument(
        "--no-clear", action="store_true", help="don't clear clipboard after copy"
    )
    cp_sp.set_defaults(func=clipboard)

    ######### autotype
    at_sp = add_parser(
        "autotype",
        help="Auto-type sequence of entry fields.",
        description="This simulates keypresses to any currently open window. "
        "It's particularily useful when kpsh is run from a script "
        "or keypress in non-interactive mode (`-c` switch). If "
        "`-s` is given, it will be used as auto-type sequence. "
        "Otherwise sequence defined for selected entry will be "
        "used or the default one if there is none (`-d`).",
    )
    at_sp.add_argument("path", help="path of entry to auto-type")
    at_sp.add_argument("-s", "--sequence", help="override auto-type sequence")
    at_sp.add_argument(
        "-d",
        "--default",
        default="{USERNAME}{TAB}{PASSWORD}{ENTER}",
        help="default auto-type sequence used when entry doesn't specify "
        "sequence itself.",
    )
    at_sp.add_argument(
        "-D", "--delay", type=int, default=40, help="delay beteen simulated keypresses"
    )
    at_sp.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="force auto-type for entries for which auto-type was disabled",
    )
    at_sp.add_argument(
        "-b",
        "--backend",
        choices=("xdotool", "ydotool", "wtype"),
        help="force usage of backend program for typing",
    )
    at_sp.add_argument(
        "-B",
        "--backend-command",
        help="command which will be run before autotype to detect backend. It "
        "should print the backend name (see --backend) to the standard "
        "output.",
    )
    at_sp.set_defaults(func=autotype)

    ######### exit
    exit_sp = add_parser("exit", help="Exit shell.")
    exit_sp.set_defaults(func=exit)

    ######### echo
    echo_sp = add_parser("echo", help="Display a message.")
    echo_sp.add_argument("message", nargs="*", help="message to be displayed")
    echo_sp.set_defaults(func=echo)

    ######### sleep
    sleep_sp = add_parser(
        "sleep",
        help="Sleep for a given number of seconds.",
        description="Seconds might be a floating number when fractions of "
        "second are needed.",
    )
    sleep_sp.add_argument("secs", type=float, help="seconds to sleep")
    sleep_sp.set_defaults(func=sleep)

    ######### help
    help_sp = add_parser("help", help="Show help for any command.")
    help_sp.add_argument("command", nargs="?")
    help_sp.set_defaults(func=lambda *a, parsers=parsers: help_(*a, parsers))

    return cp, parsers


def tokenize(seq):
    tokens = []

    i = 0
    while i < len(seq):
        start = seq.find("{", i)

        if start != -1:
            if i < start:
                tokens.append(seq[i:start])

            end = seq.find("}", start)
            nend = end + 1

            if end == -1:
                end = len(seq) - 1
            elif end == start + 1 and len(seq) > nend and seq[nend] == "}":  # {}}
                end = nend

            tokens.append(seq[start : end + 1])
            i = end + 1
        else:
            tokens.append(seq[i:])
            i = len(seq)

    return tokens


def autotype_environment(backend, backend_command, ioh):
    def _xdotool():
        from kpsh.autotype.xdotoolkeys import XDOTOOL_KEYS
        from kpsh.autotype.commands import xdotool_type, xdotool_key

        return xdotool_type, xdotool_key, XDOTOOL_KEYS

    def _ydotool():
        from kpsh.autotype.ydotoolkeys import YDOTOOL_KEYS
        from kpsh.autotype.commands import ydotool_type, ydotool_key

        return ydotool_type, ydotool_key, YDOTOOL_KEYS

    def _wtype():
        from kpsh.autotype.wtypekeys import WTYPE_KEYS
        from kpsh.autotype.commands import wtype_type, wtype_key

        return wtype_type, wtype_key, WTYPE_KEYS

    if not backend and backend_command:
        cmd = shlex.split(backend_command)
        try:
            cp = subprocess.run(cmd, capture_output=True, text=True)
            if cp.returncode == 0:
                backend = cp.stdout.strip().lower()
        except:
            ioh.eprint("Failed to run backend-cmd: {}".format(backend_command))

    # backend-command was not set, or it failed - fall back to auto-detection
    if not backend:
        backend = detect_environment()

    backend_map = {
        "xdotool": _xdotool,
        "ydotool": _ydotool,
        "wtype": _wtype,
        (OS.Linux, Environment.X11): _xdotool,
        (OS.Linux, Environment.Wayland): _ydotool,
    }

    backend_fn = backend_map.get(backend, _xdotool)
    return backend_fn()


def generate_password(characters, length):
    unique_chars = list(set(characters))
    password = "".join(secrets.choice(unique_chars) for i in range(length))
    return password


def generate_password_confirm(characters, length, ioh, confirm):
    while True:
        password = generate_password(characters, length)

        if not confirm:
            return password

        ioh.print(f"Generated password: {password}")
        repl = prompt_repeat(ioh, "[A]ccept/[N]ext/[C]ancel", "aAnNcC").lower()

        if repl == "a":
            return password
        elif repl == "c":
            return None


def askpass(ioh, prompt="Password"):
    return ioh.prompt("{}: ".format(prompt), is_password=True)


def prompt_repeat(ioh, prompt, allowed_replies, case_sensitive=True):
    while True:
        repl = ioh.prompt(f"{prompt}: ")
        if repl and repl in allowed_replies:
            return repl


def clipboard(kp, args, ioh):
    if args.no_clear:
        args.clear_after = 0

    tname = "clipboard-clear"
    timer = threads.find_thread(tname)

    entry = _get(args.path, kp)

    with reraise_as(CommandError, eins=[OSError, subprocess.SubprocessError]):
        copy_to_clipboard(getattr(entry, args.field), args.clear_after)
        if timer:
            # Philosophical question: is threading.Timer.function a public, but
            # undocumented interface, or not?
            timer.cancel()
            timer.function.cancel()

        if args.clear_after > 0:
            threads.run_later(tname, args.clear_after, cleanup(clear_clipboard))
            ioh.print(
                f"{args.field} copied to clipboard, clear after {args.clear_after} seconds"
            )
        else:
            ioh.print(f"{args.field} copied to clipboard")


def autotype(kp, args, ioh):
    from kpsh.autotype.placeholders import replace_placeholder
    from kpsh.autotype.commands import run_command

    delay = str(args.delay)
    entry = _get(args.path, kp)

    if not entry.autotype_enabled and not args.force:
        ioh.eprint(
            "Autotype disabled for {}. " "Use -f to force autotype.".format(args.path)
        )
        return

    sequence = args.sequence if args.sequence else entry.autotype_sequence
    if not sequence:
        sequence = args.default

    typecmd, keycmd, TOOL_KEYS = autotype_environment(
        args.backend, args.backend_command, ioh
    )

    for token in tokenize(sequence):
        if token.startswith("{") and token.endswith("}"):
            if run_command(token):
                continue

            placeholder = replace_placeholder(entry, token)
            if placeholder is not None:
                typecmd(delay, placeholder)
                continue

            specialkey = TOOL_KEYS.get(token)
            if specialkey is not None:
                keycmd(delay, specialkey)
                continue

            ioh.eprint("Unsupported keyword: {}".format(token))
        else:
            typecmd(delay, token)


def notes_deleter(spec):
    def _delete_all(notes):
        return []

    # range is inclusive on both sides, so for example range 1-3 will delete
    # notes 1, 2 and 3
    def _delete_range(notes, start, end):
        return [note for i, note in enumerate(notes) if (i < start or i > end)]

    if spec == "*":
        return _delete_all

    if "-" in spec:
        start, _, end = spec.partition("-")
        start = int(start.strip())
        end = int(end.strip())
    else:
        start = int(spec.strip())
        end = start

    if start <= 0 or end <= 0:
        raise ValueError("Invalid range (must be > 0): {} - {}".format(start, end))

    return lambda notes: _delete_range(notes, start - 1, end - 1)


def show(kp, args, ioh):
    def _print_single(spec, attr):
        ioh.print(spec.format(name=attr.name, value=attr.value))

    def _print_list(spec, attr):
        for i, elem in enumerate(attr.value):
            indexed_name = "{name}[{i}]".format(name=attr.name, i=i + 1)
            ioh.print(spec.format(name=indexed_name, value=elem))

    def _print_multiline(spec, attr):
        for i, elem in enumerate(attr.value.splitlines()):
            indexed_name = "{name}[{i}]".format(name=attr.name, i=i + 1)
            ioh.print(spec.format(name=indexed_name, value=elem))

    entry = _get(args.path, kp)
    Attr = collections.namedtuple("Data", ("name", "value", "printer"))

    attrs = [
        Attr("path", args.path, _print_single),
        Attr("username", entry.username, _print_single),
        Attr("password", entry.password, _print_single),
        Attr("url", entry.url, _print_single),
        Attr("autotype_sequence", entry.autotype_sequence, _print_single),
        Attr("notes", entry.notes, _print_list),
    ]

    for pname, pval in entry.custom_properties.items():
        attrs.append(Attr(f"p:{pname}", pval, _print_multiline))

    def find_attr(name):
        # This function tries to find fields intelligently. Users can prefix
        # field names with e.g. "p:" to indicate a property, but if they don't,
        # the function will search for unmarked properties anyway, when their
        # names don't collide with regular fields.
        pname = name if name.startswith("p:") else f"p:{name}"
        possible_property = None

        for attr in attrs:
            if attr.name == name:
                return attr
            if attr.name == pname:
                possible_property = attr
        return possible_property

    fields = args.fields if args.fields else [a.name for a in attrs]

    for field in fields:
        attr = find_attr(field)
        if attr is None:
            ioh.eprint("Unknown attribute: {}".format(field))
            continue

        if attr.value is None:
            continue

        spec = "{value}" if args.no_field_name else "{name}: {value}"
        attr.printer(spec, attr)


def _get_properties(properties):
    properties = properties or []
    for prop in properties:
        key, delim, val = prop.partition("=")

        if not key:
            raise KeyError(f"Custom property '{prop}' must have a name.")

        if not delim:
            raise KeyError(
                f"Custom property '{key}' must be constructed as name=value."
            )

        val = val.replace("\\n", "\n").replace("\\r", "\r")
        yield key, val


def add(kp, args, ioh):
    if args.path in kp.entries:
        raise CommandError("entry already exists: {}".format(args.path))

    if args.password is None and args.pw_gen:
        characters = None
        if args.characters:
            characters = args.characters
        elif args.charset:
            characters = "".join(args.charset)
        else:
            characters = string.ascii_letters + string.digits
        confirm = args.pw_gen == "interactive"
        args.password = generate_password_confirm(characters, args.length, ioh, confirm)
        if args.password is None:  # cancel
            return
    elif args.password is None:
        prompt = "Password for new entry"
        args.password = askpass(ioh, prompt)

    with reraise_as(CommandError):
        with kp.no_reload():
            entry = kp.open_entry(args.path, create=True, exclusive=True)
            with stop_on_error(kp.delete_entry, entry):
                for field in [
                    "username",
                    "password",
                    "url",
                    "notes",
                    "autotype_sequence",
                ]:
                    val = getattr(args, field)
                    setattr(entry, field, val)

                for pname, pval in _get_properties(args.properties):
                    entry.set_custom_property(pname, pval)

    kp.save()


def edit(kp, args, ioh):
    entry = _get(args.path, kp)

    if args.password is None and args.askpass:
        prompt = "New password for {}".format(entry.title)
        args.password = askpass(ioh, prompt)
    elif args.password is None and args.pw_gen:
        characters = None
        if args.characters:
            characters = args.characters
        elif args.charset:
            characters = "".join(args.charset)
        else:
            characters = string.ascii_letters + string.digits
        confirm = args.pw_gen == "interactive"
        args.password = generate_password_confirm(characters, args.length, ioh, confirm)
        if args.password is None:  # cancel
            return

    old_notes = entry.notes or []

    if args.delnotes:
        with reraise_as(
            CommandError,
            msg=f"Invalid value for -N: {args.delnotes}",
            eins=(ValueError, TypeError),
        ):
            deleter = notes_deleter(args.delnotes)
            old_notes = deleter(old_notes)

    new_notes = args.notes or []
    notes = old_notes + new_notes

    element_copy = deepcopy(entry._entry._element)
    entry.save_history()

    with reraise_as(CommandError):
        with stop_on_error(_restore_entry, entry, element_copy):
            for field in ["username", "password", "url", "autotype_sequence"]:
                val = getattr(args, field)
                setattr(entry, field, val)

            entry.notes = notes

            for pname, pval in _get_properties(args.properties):
                entry.set_custom_property(pname, pval)

    if entry.modified:
        entry.touch(modify=True)
        kp.save()
    else:
        _delete_last_history(entry)


def delete(kp, args, ioh):
    deleted = False
    with kp.no_reload():
        for path in args.paths:
            path = path.rstrip("/")
            if path in kp.entries:
                entry = kp.delete_entry(path)
                deleted |= bool(entry)
            elif path in kp.groups:
                if not args.recursive:
                    ioh.eprint(
                        f"Cannot delete group {path}. Use --recursive to delete it."
                    )
                    continue

                deleted |= kp.delete_group(path)
            else:
                ioh.eprint(f"Cannot delete {path}: path doesn't exist in database.")

    if deleted:
        kp.save()


def move(kp, args, ioh):
    title = args.source.rsplit("/")[-1]
    group = kp.find_group(args.dest)
    dest_path = f"{args.dest}/{title}" if group else args.dest

    entry = _get(args.source, kp)
    entry.save_history()

    try:
        moved = kp.move_entry(args.source, dest_path)
    except AttributeError as e:
        _delete_last_history(entry)
        raise CommandError(str(e))

    moved.touch(modify=True)
    kp.save()


def echo(kp, args, ioh):
    ioh.print(*args.message)


def sleep(kp, args, ioh):
    time.sleep(args.secs)


def ls(kp, args, ioh):
    # TODO: replace with a proper, less complex solution
    # w/a for double-printing about unopened databases (because kp.groups and
    # then kp.iter_paths will both try to kp.unlock())
    if not kp.unlock():
        return

    if args.glob.endswith("/"):
        args.glob = args.glob.rstrip("/")
    if args.glob in kp.groups:
        args.glob = f"{args.glob}/*"

    for path in fnmatch.filter(kp.iter_paths(), args.glob):
        ioh.print(path)


def help_(kp, args, ioh, parsers):
    parser = parsers.get(args.command)
    if parser is None:
        ioh.eprint("No such command: {}".format(args.command))
        parser = parsers.get(None)

    parser.print_help()


def exit(kp, args, ioh):
    ioh.stop()


def open_(kp, args, ioh):
    fp = os.path.expanduser(args.filepath)
    kp.change_db(fp)


def unlock(kp, args, ioh):
    if not kp.locked:
        return

    kf = os.path.expanduser(args.keyfile) if args.keyfile else None
    if kf:
        kp.change_credentials(keyfile=kf)

    kp.unlock()


def lock(kp, args, ioh):
    kp.lock()


def db(kp, args, ioh):
    ioh.print(kp.db)
    ioh.print("Locked: {}".format(kp.locked))


def _restore_entry(entry: EntryProxy, element):
    # TODO: This uses internal pykeepass's lxml.etree.Element. I've found no
    # other way to exactly revert changes. If there appears a public API for
    # such tasks, we should use it (mgoral, 2024-01-26)
    entry._entry._element = element


def _delete_last_history(entry):
    last = entry.history[-1]
    entry.delete_history(last)


def _get(path, kp):
    entry = kp.open_entry(path)
    if not entry:
        raise CommandError("Entry not found: {}".format(path))
    return entry
