import os
import string

import pytest

from kpsh.commands import CommandError


@pytest.fixture
def kpbig(kp_factory):
    return kp_factory("db_argon2_kdbx4_pass_big.kdbx", password="foobar")


@pytest.mark.parametrize(
    "src,dst",
    [("foo", "moved_foo"), ("foo", "newgroup/blah"), ("foo", "group/baba")],
)
def test_move(kpbig, th, src, dst):
    expected = th.fields(src, kpbig.kp).copy()
    del expected["path"]

    th.cmd(f"move '{src}' '{dst}'", kpbig.kp, kpbig.ioh)

    assert src not in kpbig.kp.entries
    assert dst in kpbig.kp.entries

    moved = th.fields(dst, kpbig.kp)
    moved_path = moved.pop("path")

    assert moved_path == dst
    assert moved == expected


def test_move_to_group(kpbig, th):
    expected = th.fields("foo", kpbig.kp).copy()
    del expected["path"]
    group = kpbig.kp.groups[0]
    expected_moved_path = f"{group}/foo"

    th.cmd(f"move 'foo' '{group}'", kpbig.kp, kpbig.ioh)

    assert "foo" not in kpbig.kp.entries
    assert expected_moved_path in kpbig.kp.entries

    moved = th.fields(expected_moved_path, kpbig.kp)
    moved_path = moved.pop("path")

    assert moved_path == f"{group}/foo"
    assert moved == expected


@pytest.mark.parametrize(
    "src,dst",
    [
        ("unexisting_entry", "something_else"),
        ("foo", "other"),
        ("foo", "other/foo"),
        ("foo", "foo"),
    ],
)
def test_move_fail(kpbig, th, src, dst):
    with pytest.raises(CommandError):
        th.cmd(f"move '{src}' '{dst}'", kpbig.kp, kpbig.ioh)


def test_move_saves_history(kpbig, th):
    assert not kpbig.kp.entries["foo"].history

    th.cmd("move foo foo_moved", kpbig.kp, kpbig.ioh)

    history = kpbig.kp.entries["foo_moved"].history[-1]
    assert history.title == "foo"


@pytest.mark.parametrize("dst", ["other", "other/foo", "foo"])
def test_invalid_move_doesnt_change_history(kpbig, th, dst):
    assert not kpbig.kp.entries["foo"].history
    with pytest.raises(CommandError):
        th.cmd(f"move foo '{dst}'", kpbig.kp, kpbig.ioh)
    assert not kpbig.kp.entries["foo"].history
