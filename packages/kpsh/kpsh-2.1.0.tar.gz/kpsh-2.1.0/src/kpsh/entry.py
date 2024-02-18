# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2024 Michał Góral.

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pykeepass.entry import Entry


class _Converter:
    def restore(self, val):
        """Used to restore value of original entry to the format used by kpsh"""
        return val

    def convert(self, val):
        """Used to convert kpsh format to the format used by pykeepass"""
        return val


class _Str2List(_Converter):
    def restore(self, val):
        if isinstance(val, str):
            return val.splitlines()
        return val

    def convert(self, val):
        if isinstance(val, (list, tuple)):
            val = "\n".join(val)
        return val


class _FieldProxy:
    def __init__(self, conv=_Converter()):
        self._name = None
        self._conv = conv

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, objtype=None):
        val = getattr(obj.realentry, self._name)
        return self._conv.restore(val)

    def __set__(self, obj, value):
        oldval = getattr(obj.realentry, self._name)
        newval = self._conv.convert(value)
        if _value_changed(newval, oldval):
            setattr(obj._entry, self._name, newval)
            obj._mod = True


class EntryProxy:
    """Proxy to pykeepass.Entry object which adds some auto-validation and
    conversion methods between types stored in KeePass databases and used by
    kpsh. It disallows setting fields to None (pykeepass converts it to 'None'
    string) and keeps track of changes."""

    __slots__ = ("_entry", "_mod")

    def __init__(self, entry: "Entry"):
        self._entry = entry
        self._mod = False

    def __getattr__(self, name):
        return getattr(self._entry, name)

    # Thanks to __slots__, we may control which fields can be used. Even if
    # underlying Entry supports more fields than the following list, access to
    # them will lead to errors without adding explicit support here.
    title = _FieldProxy()
    username = _FieldProxy()
    password = _FieldProxy()
    url = _FieldProxy()
    notes = _FieldProxy(conv=_Str2List())
    autotype_sequence = _FieldProxy()

    def set_custom_property(self, key, value, *args, **kwargs):
        oldval = self.realentry.get_custom_property(key)
        if _value_changed(value, oldval):
            self.realentry.set_custom_property(key, value, *args, **kwargs)
            self._mod = True

    @property
    def realentry(self):
        return self._entry

    @property
    def modified(self):
        return self._mod

    def __eq__(self, other):
        if isinstance(other, EntryProxy):
            return self._entry.__eq__(other._entry)
        return False

    def __ne__(self, other):
        if isinstance(other, EntryProxy):
            return self._entry.__ne__(other._entry)
        return False

    def __hash__(self):
        return self._entry.__hash__()

    def __repr__(self):
        p = "/".join(self.realentry.path or ["/"])
        return f"EntryProxy({p})"


def _value_changed(newval, oldval):
    # Rules:
    # 1. disallow setting fields to None; even though most of PyKeePass' fields
    #    have it as a default value, PyKeePass does little to no validation when
    #    writing XML and fails miserably when None is used.
    # 2. some empty fields (like notes) can be either None or empty string, so
    #    changing from None to empty string should return False
    return newval is not None and newval != oldval and (bool(newval) or bool(oldval))
