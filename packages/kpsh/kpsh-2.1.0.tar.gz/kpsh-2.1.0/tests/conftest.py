import os
import shutil
import re
import shlex
from functools import cache, partial
from collections import namedtuple

import pytest
from unittest.mock import Mock

from kpsh.commands import prepare_command_parser, CommandError
from kpsh.db import DelayedPyKeePass
from kpsh.io import Handler


class ProgrammableIO(Handler):
    def __init__(self):
        self.prompt = Mock()
        self.print = Mock()
        self.eprint = Mock()
        self.get_command = Mock()
        super().__init__()


class Args:
    def __getattr__(self, name):
        return self.__dict__.get(name, None)


def copy_db_data(dbname, destdir):
    curdir = os.path.dirname(os.path.abspath(__file__))

    keysrc = os.path.join(curdir, "db", "keyfile")
    keydst = os.path.join(destdir, "keyfile")
    shutil.copy(keysrc, keydst)

    src = os.path.join(curdir, "db", dbname)
    dst = os.path.join(destdir, dbname)
    shutil.copy(src, dst)
    return dst


def make_kpdata(**kw):
    Data = namedtuple("Data", ("kp", "args", "ioh"))

    iohandler = ProgrammableIO()

    args = Args()
    args.__dict__.update(kw)

    kp = DelayedPyKeePass(args, iohandler)

    return Data(kp, args, iohandler)


@pytest.fixture
def iohandler():
    return ProgrammableIO()


@pytest.fixture
def fakeargs():
    return Args()


@pytest.fixture
def tmpdb(tmpdir):
    factory = partial(copy_db_data, destdir=str(tmpdir))
    return factory


@pytest.fixture
def kp_factory(tmpdb):
    def factory(dbpath, **args):
        db = tmpdb(dbpath)
        return make_kpdata(db=db, **args)

    return factory


@pytest.fixture
def kp_open():
    def opener(path, **args):
        return make_kpdata(db=path, **args)

    return opener


@pytest.fixture(scope="session")
def shared_tmpdb(tmpdir_factory):
    tmpdir = tmpdir_factory.mktemp("databases")
    factory = partial(copy_db_data, destdir=tmpdir)
    return factory


# opening databases is slow... so we introduce a shared DelayedPyKeePass, which
# can be accessed by a few different tests. Generally it should be used only to
# test read-only operations (not counting unlocking, because usually it doesn't
# hurt that database has been unlocked in some other test)
@pytest.fixture(scope="session")
def shared_kp_factory(shared_tmpdb):
    @cache
    def factory(dbpath, **args):
        db = shared_tmpdb(dbpath)
        return make_kpdata(db=db, **args)

    return factory


class Helpers:
    @staticmethod
    def cmd(text, kp, ioh):
        parser, _ = prepare_command_parser()
        text_spl = shlex.split(text) if isinstance(text, str) else text
        args = parser.parse_args(text_spl)
        return args.func(kp, args, ioh)

    @staticmethod
    def fields(path, kp):
        fields = {}

        def store_field(arg):
            # name: val
            # p:name: val
            kvm = re.match(r"((?:p:)?[^:]+):(.*)", arg)
            key = kvm[1]
            val = kvm[2]

            # examples of keys: path, notes[1], p:property[1]
            m = re.match(r"([^[]+)(?:\[(\d+)\])?", key)

            key = m[1].strip()
            id = m[2]
            val = val[1:]  # strip the initial space added by kpsh

            if id is not None:
                vals = fields.setdefault(key, [])
                vals.append(val)
                assert int(id) == len(vals)
            else:
                fields[key] = val

        ioh = ProgrammableIO()
        ioh.print.side_effect = store_field

        try:
            Helpers.cmd(f"show {path}", kp, ioh)
        except CommandError:
            return None

        return fields

    @staticmethod
    def assert_fields_dct(kp, path, fields):
        fields.setdefault("path", path)
        existing_fields = Helpers.fields(path, kp)
        assert fields is not None, f"entry '{path}' doesn't exist in database"
        assert fields == existing_fields

    @staticmethod
    def assert_fields(kp, path, **fields):
        return Helpers.assert_fields_dct(kp, path, fields)


@pytest.fixture
def th():
    return Helpers
