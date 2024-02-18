import os
import string

import pytest

from kpsh.commands import CommandError


@pytest.mark.parametrize(
    "kwargs", [{"password": "foobar"}, {"pw_cmd": "printf foobar"}]
)
def test_unlock_lock_proceture(kp_factory, th, kwargs):
    kp = kp_factory("db_argon2_kdbx4_pass.kdbx", **kwargs)
    assert kp.kp.locked

    th.cmd("unlock", kp.kp, kp.ioh)
    assert not kp.kp.locked

    th.cmd("lock", kp.kp, kp.ioh)
    assert kp.kp.locked
    kp.ioh.prompt.assert_not_called()

    kp.ioh.prompt.return_value = "blaz"
    th.cmd("unlock", kp.kp, kp.ioh)
    kp.ioh.prompt.assert_called_once()
    assert kp.kp.locked

    kp.ioh.prompt.return_value = "foobar"
    th.cmd("unlock", kp.kp, kp.ioh)
    assert not kp.kp.locked


def test_unlock_keyfile(kp_factory, th):
    kp = kp_factory("db_argon2_kdbx4_pass_keyfile.kdbx", password="foobar")
    keyfile = os.path.join(os.path.dirname(kp.kp.db), "keyfile")

    # missing keyfile - kpsh will be unable to unlock the database and will
    # ask for a password (it doesn't know that lack of keyfile is the
    # reason for unlock fail)
    th.cmd("unlock", kp.kp, kp.ioh)
    kp.ioh.prompt.assert_called_once()
    assert kp.kp.locked

    # kpsh shouldn't overwrite the password. Unlock allows changing the
    # keyfile, so it should set it and then proceed successfully
    kp.ioh.prompt.reset_mock()
    th.cmd(f"unlock --keyfile '{keyfile}'", kp.kp, kp.ioh)
    kp.ioh.prompt.assert_not_called()
    assert not kp.kp.locked

    # locking clears credentials
    th.cmd("lock", kp.kp, kp.ioh)
    assert kp.kp.locked

    # the same situation as in the first unlock: lock of database should
    # clear all stored credentials (password, keyfile), so kpsh doesn't
    # know about keyfile from now on.
    kp.ioh.prompt.reset_mock(return_value="foobar")
    th.cmd("unlock", kp.kp, kp.ioh)
    kp.ioh.prompt.assert_called_once()
    assert kp.kp.locked

    # unlock with --keyfile and without a stored password should now
    # interactively ask for password
    kp.ioh.prompt.reset_mock(return_value="foobar")
    th.cmd(f"unlock --keyfile '{keyfile}'", kp.kp, kp.ioh)
    kp.ioh.prompt.assert_called_once()
    assert kp.kp.locked
