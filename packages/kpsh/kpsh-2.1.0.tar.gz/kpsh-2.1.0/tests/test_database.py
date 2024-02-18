import os
import pytest

from kpsh.db import DelayedPyKeePass


@pytest.fixture
def kp(kp_factory):
    def opener(**args):
        return kp_factory("db_argon2_kdbx4_pass.kdbx", **args)

    return opener


def test_states(kp):
    kp = kp(password="foobar").kp
    assert kp.locked
    assert kp.unlock()
    assert not kp.locked


def test_fail_unlock(kp):
    kp = kp().kp
    assert not kp.unlock()


def test_unlock_of_unlocked_db(kp):
    kpdata = kp()
    kp = kpdata.kp
    ioh = kpdata.ioh

    ioh.prompt.return_value = "foobar"
    assert kp.unlock()

    ioh.prompt.return_value = None
    assert kp.unlock()


def test_auto_reload(kp):
    kpdata = kp()
    kp = kpdata.kp
    ioh = kpdata.ioh
    args = kpdata.args

    ioh.prompt.return_value = "foobar"

    assert kp.unlock()
    assert kp.kp

    # Let's change the passwords so we can verify that auto-reloading fails
    kp.kp.password = None
    ioh.prompt.return_value = None

    # Modify mtime of our database
    curr = os.stat(args.db)
    os.utime(args.db, (curr.st_atime, curr.st_mtime + 100))

    assert not kp.kp  # failed auto-unlocking because we removed password

    ioh.prompt.return_value = "foobar"
    assert kp.kp
