# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2019 Michał Góral.

from typing import Union, Optional


import os
import subprocess
import operator
import collections
import contextlib
from datetime import datetime as dt

from kpsh.entry import EntryProxy


EntryOrPath = Union[str, EntryProxy]


class DatabaseError(Exception):
    pass


class UNSET:
    pass


# Delays importing of PyKeePass which by itself adds ~150 ms to startup...
class DelayedPyKeePass:
    def __init__(self, args, ioh):
        self._db = None
        self._ioh = ioh
        if args.db:
            self.change_db(args.db)

        self._password = args.password
        self._keyfile = args.keyfile

        self._pw_cmd = args.pw_cmd
        self._pinentry = args.pinentry

        self._kp = None
        self._mtime = None
        self._entries = None
        self._reload_guard = 0

    def _getpass(self):
        if self._password is not None:
            yield self._password
        if self._pw_cmd is not None:
            yield readpass(self._pw_cmd)
        if (
            self._password is None
            and self._pw_cmd is None
            and self._keyfile is not None
        ):
            # password=None supports Composite Master Key with only a keyfile
            # https://keepass.info/help/base/keys.html
            yield None
        yield askpass(self._db, self._pinentry, self._ioh)

    def unlock(self):
        if self._kp and self._reload_guard > 0:
            return True

        if self._kp and self._mtime == self._read_mtime():
            return True
        if self._kp:
            # If e.g. database password was changed, this might fail. That's OK,
            # but we must allow user to provide a password in a second,
            # "ordinary" database read.
            if self._read_db([self._kp.password], self._kp.keyfile):
                return True
            self._ioh.eprint(
                "Database was modified externally and must be reloaded, "
                "but auto-reload failed. Re-obtaining password."
            )

        if not self._db:
            self._ioh.eprint("No database is selected.")
            return False

        if not self._read_db(self._getpass, self._keyfile):
            self._ioh.eprint("Failed unlocking database {}.".format(self._db))
            return False
        return True

    def lock(self):
        self._kp = None
        self._entries = None
        self._password = None
        self._pw_cmd = None
        self._keyfile = None

    def change_db(self, db):
        self.lock()
        if not os.path.isfile(db) and os.path.exists(db):
            self._ioh.eprint("Invalid database: '{}'".format(db))
            return
        if not os.path.exists(db):
            self._ioh.eprint(
                "Database doesn't exist and will be created on the first use: "
                "{}.".format(db)
            )
        self._db = db

    def change_credentials(self, password=UNSET, keyfile=UNSET):
        if not self.locked:
            raise DatabaseError(
                "Database must be locked before changing credentials "
                "used for unlocking."
            )

        if password is not UNSET:
            self._password = password
        if keyfile is not UNSET:
            self._keyfile = keyfile

    @property
    def locked(self):
        return self._kp is None

    @property
    def db(self):
        return self._db

    @property
    def kp(self):
        self.unlock()
        return self._kp

    @property
    def entries(self):
        if not self.kp:
            return collections.OrderedDict()

        if self._entries is None:
            self._entries = collections.OrderedDict(
                ("/".join(e.path), EntryProxy(e))
                for e in sorted(self.kp.entries, key=operator.attrgetter("path"))
            )

        return self._entries

    @property
    def paths(self):
        return [e for e in self.entries.keys()]

    def iter_paths(self):
        for entry in self.entries:
            yield entry

    def add_group(self, path):
        kp = self.kp

        if not kp:
            return None

        if not path:
            raise ValueError("Unexpected empty path")

        path = path.split("/")
        curr = kp.root_group

        for part in path:
            found = kp.find_groups(name=part, group=curr, recursive=False, first=True)
            if found:
                curr = found
            else:
                curr = kp.add_group(curr, part)

        return curr

    def find_group(self, path):
        return self.kp.find_groups(path=path.split("/"))

    @property
    def root_group(self):
        if not self.kp:
            return None
        return self.kp.root_group

    def open_entry(self, path, create=False, exclusive=False):
        entry = self.entries.get(path)
        if entry:
            if create and exclusive:
                raise DatabaseError(f"entry already exists: {path}")
            return entry

        if create:
            groupname, _, title = path.rpartition("/")
            if not title:
                raise CommandError("Empty titles are not allowed")
            group = self.add_group(groupname) if groupname else self.root_group
            entry = EntryProxy(
                self.kp.add_entry(group, title, username="", password="")
            )
            self.reload_entries()
            return entry

        return None

    def move_entry(self, source_path, destination_path):
        if destination_path in self.entries:
            raise AttributeError(f"{destination_path} already exists")
        if not source_path in self.entries:
            raise AttributeError(f"{source_path} doesn't exists")

        kp = self.kp

        source = self.entries[source_path]
        groupname, _, title = destination_path.rpartition("/")
        group = self.add_group(groupname) if groupname else kp.root_group

        source.save_history()

        source.title = title
        self.kp.move_entry(source, group)

        self.reload_entries()
        return source

    def delete_entry(self, entry: EntryOrPath) -> Optional[EntryProxy]:
        if isinstance(entry, str):
            entry = self.entries.get(entry)

        if not isinstance(entry, EntryProxy):
            raise TypeError("unexpected entry type")

        if entry:
            self.kp.delete_entry(entry.realentry)
            self.reload_entries()
            return entry
        return None

    def delete_group(self, path):
        group = self.find_group(path)
        if group:
            self.kp.delete_group(group)
            self.reload_entries()
            return True
        return False

    @property
    def groups(self):
        kp = self.kp
        if not kp:
            return []
        return ["/".join(g.path) for g in self.kp.groups if g.path]

    def save(self):
        assert self._kp, "database not opened before save() call"
        assert (
            self._reload_guard == 0
        ), "save() can't be called when no_reload is active"

        if self._mtime != self._read_mtime():
            newf = next_file(self._kp.filename)
            self._kp.save(newf)
            self._kp.filename = newf
            self._db = newf
            self._mtime = self._read_mtime()
            self._ioh.eprint(
                "Database was modified externally. To prevent data loss, "
                "changes were saved to the new database: {}".format(newf)
            )
            return

        self._kp.save()
        self._mtime = self._read_mtime()

    @contextlib.contextmanager
    def no_reload(self):
        try:
            self._reload_guard += 1
            yield
        finally:
            self._reload_guard -= 1

    def reload_entries(self):
        self._entries = None

    def _read_mtime(self):
        return os.stat(self._db).st_mtime

    def _read_db(self, password_iter, keyfile):
        from pykeepass import PyKeePass, create_database

        if callable(password_iter):
            password_iter = password_iter()

        def _open_db(password, keyfile):
            if os.path.exists(self._db):
                kp = PyKeePass(self._db, password=password, keyfile=keyfile)
            else:
                kp = create_database(self._db, password=password, keyfile=keyfile)
                pwfmt = "<redacted>" if password else "<empty>"
                kwfmt = keyfile if keyfile else "<none>"
                self._ioh.eprint(
                    "Database created: {db} (password: {pw}, keyfile: {kf})".format(
                        db=self._db, pw=pwfmt, kf=kwfmt
                    )
                )
            return kp

        kp = None
        for pw in password_iter:
            try:
                kp = _open_db(password=pw, keyfile=keyfile)
            except Exception as e:
                pass
            else:
                self._mtime = self._read_mtime()
                break

        self._kp = kp
        self._entries = None
        return kp is not None


def askpass(db, pinentry, ioh):
    if pinentry:
        return _askpass_pinentry(db, pinentry)
    return _askpass_prompt(ioh)


def readpass(cmd):
    cp = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if cp.returncode != 0 or not cp.stdout:
        return None
    return cp.stdout


def next_file(path):
    while True:
        ts = dt.now().timestamp()
        nextf = "{}~{}".format(path, ts)
        if not os.path.exists(nextf):
            return nextf


def _askpass_pinentry(db, pinentry):
    pein = "setdesc Enter password for {}\ngetpin\n".format(db)
    cp = subprocess.run(pinentry, input=pein, capture_output=True, text=True)

    if cp.returncode != 0 or not cp.stdout:
        return None

    lines = cp.stdout.splitlines()
    dlines = [line for line in lines if line.startswith("D ")]
    if not dlines:
        return None

    passline = dlines[0]
    return passline.partition(" ")[-1]


def _askpass_prompt(ioh):
    return ioh.prompt("Database password: ", is_password=True)


def _field_changed(newval, oldval):
    # Rules:
    # 1. disallow setting fields to None; even though most of PyKeePass' fields
    #    have it as a default value, PyKeePass does little to no validation when
    #    writing XML and fails miserably when None is used.
    # 2. some empty fields (like notes) can be either None or empty string, so
    #    changing from None to empty string should return False
    return newval is not None and newval != oldval and (bool(newval) or bool(oldval))
