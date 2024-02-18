# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2019 Michał Góral.

import os
import sys
import argparse
import tempfile
import signal

from kpsh.io import Interactive, NonInteractive, Daemon, Arguments

from kpsh import __version__ as _version
from kpsh import threads
from kpsh.db import DelayedPyKeePass
from kpsh.commands import prepare_command_parser
from kpsh.cleanup import cleanup


def sysexit(signum, frame):
    raise SystemExit(128 + signum)


def default_socket_path():
    tmp = tempfile.gettempdir()
    fname = "kpsh-{}.sock".format(os.getuid())
    return os.path.join(tmp, fname)


def prepare_args():
    ap = argparse.ArgumentParser(description="KeePass database shell access.")
    ap.add_argument("db", nargs="?", help="path to KeePass database.")

    ap.add_argument("--password", default=None, help="Database password.")
    ap.add_argument(
        "--password-command",
        dest="pw_cmd",
        default=None,
        help="Password will be obtained from the output of this command.",
    )
    ap.add_argument("--keyfile", default=None, help="Key file for unlocking database.")
    ap.add_argument("--pinentry", help="Command used to run pinentry.")
    ap.add_argument(
        "-c",
        "--command",
        action="append",
        help="Command to execute. If command arguments contain spaces, they "
        "must be enclosed in double quotes. With this switch, kpsh will be "
        "started in non-interactive mode. A list of available commands can "
        "be found by running 'kpsh -c help'.",
    )
    ap.add_argument(
        "--prompt",
        default='<style fg="ansiblue">{}</style>> ',
        help="Text used by shell for prompt.",
    )
    ap.add_argument(
        "-d",
        "--daemon",
        action="store_true",
        help="Start as a daemon listening on a socket given by --socket-path",
    )
    ap.add_argument(
        "-s",
        "--socket-path",
        default=default_socket_path(),
        help="Path to the socket which will be created in daemon mode "
        "(default: /tmp/kpsh-$UID.sock).",
    )
    ap.add_argument(
        "--version", action="version", version="%(prog)s {}".format(_version)
    )
    return ap.parse_args()


def main():
    signal.signal(signal.SIGINT, sysexit)
    signal.signal(signal.SIGTERM, sysexit)

    args = prepare_args()

    cmd_parser, parsers = prepare_command_parser()

    cleanup(threads.stop)

    if args.command:
        ioh = Arguments(args.command)
    elif args.daemon:
        ioh = Daemon(args.socket_path)
    elif sys.stdin.isatty():
        ioh = Interactive(args.prompt, parsers)
    else:
        ioh = NonInteractive()

    with cleanup.clean_on_exit():
        kp = DelayedPyKeePass(args, ioh)
        return ioh.run(kp, cmd_parser)
