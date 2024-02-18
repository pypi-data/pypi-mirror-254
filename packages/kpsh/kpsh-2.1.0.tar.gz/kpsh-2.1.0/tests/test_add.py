import os
import string

import pytest

from kpsh.commands import CommandError


@pytest.fixture
def kpbig(kp_factory):
    return kp_factory("db_argon2_kdbx4_pass_big.kdbx", password="foobar")


def test_add_dont_override_existing_entry(kpbig, th):
    with pytest.raises(CommandError):
        th.cmd(f"add foo", kpbig.kp, kpbig.ioh)


@pytest.mark.parametrize("path", ["newentry", "group/newentry", "newgroup/entry"])
def test_add_username_password(kpbig, th, path):
    user = "myuser"
    pwd = "mypass"
    th.cmd(f"add {path} --username {user} --password {pwd}", kpbig.kp, kpbig.ioh)
    th.assert_fields(kpbig.kp, path, username=user, password=pwd)


@pytest.mark.parametrize("path", ["newentry", "group/newentry", "newgroup/entry"])
def test_add_empty_user_password(kpbig, th, path):
    kpbig.ioh.prompt.return_value = ""
    th.cmd(f"add {path} --username ''", kpbig.kp, kpbig.ioh)
    th.assert_fields(kpbig.kp, path, username="", password="")


def test_add_password_interactively(kpbig, th):
    kpbig.ioh.prompt.return_value = "newentry_password"
    th.cmd(f"add newentry", kpbig.kp, kpbig.ioh)
    th.assert_fields(kpbig.kp, "newentry", username="", password="newentry_password")


def test_add_generate_password(kpbig, th):
    th.cmd(f"add newentry --generate-password-no-confirm -l 32", kpbig.kp, kpbig.ioh)
    fields = th.fields("newentry", kpbig.kp)
    assert fields
    assert len(fields["password"]) == 32


@pytest.mark.parametrize(
    "arg,chset",
    [
        ("--letters", string.ascii_letters),
        ("--digits", string.digits),
        ("--punctuation", string.punctuation),
        ("--logograms", "#$%&@^`~"),
        ("--characters abc", ["a", "b", "c"]),
    ],
)
def test_add_generate_password_character_sets(kpbig, th, arg, chset):
    th.cmd(
        f"add newentry --generate-password-no-confirm -l 100 {arg}", kpbig.kp, kpbig.ioh
    )

    fields = th.fields("newentry", kpbig.kp)
    assert fields
    assert len(fields["password"]) == 100

    for ch in fields["password"]:
        assert (
            ch in chset
        ), f"'{ch}' is in set of letters allowed for generated password"


def test_add_generate_password_interactively(kpbig, th):
    kpbig.ioh.prompt.side_effect = ["n", "a"]
    th.cmd(f"add newentry --generate-password -l 100", kpbig.kp, kpbig.ioh)

    assert len(kpbig.ioh.print.call_args_list) == 2
    assert len(kpbig.ioh.prompt.call_args_list) == 2
    fields = th.fields("newentry", kpbig.kp)
    assert fields
    assert len(fields["password"]) == 100
    password = fields["password"]


def test_add_generate_password_interactively_cancel(kpbig, th):
    kpbig.ioh.prompt.return_value = "c"
    th.cmd(f"add newentry --generate-password -l 100", kpbig.kp, kpbig.ioh)
    assert "newentry" not in kpbig.kp.entries


def test_add_notes(kpbig, th):
    pwd = "pwd"
    th.cmd(
        f"add newentry -p {pwd} --note 'note 1' --note 'note 2'", kpbig.kp, kpbig.ioh
    )
    th.assert_fields(
        kpbig.kp, "newentry", username="", password=pwd, notes=["note 1", "note 2"]
    )


def test_add_simple_fields(kpbig, th):
    pwd = "pwd"
    th.cmd(
        f"add newentry -p {pwd} --url https://example.com --autotype-sequence {{TAB}}",
        kpbig.kp,
        kpbig.ioh,
    )
    th.assert_fields(
        kpbig.kp,
        "newentry",
        username="",
        password=pwd,
        url="https://example.com",
        autotype_sequence="{TAB}",
    )


@pytest.mark.parametrize("name,value", [("foo", "bar"), ("username", "baz")])
def test_add_property(kpbig, th, name, value):
    pwd = "pwd"
    th.cmd(
        f"add newentry -p {pwd} --property {name}={value}",
        kpbig.kp,
        kpbig.ioh,
    )

    pname = f"p:{name}"
    th.assert_fields_dct(
        kpbig.kp, "newentry", {"username": "", "password": pwd, pname: [value]}
    )


def test_add_multiline_property(kpbig, th):
    pwd = "pwd"
    th.cmd(
        f"add newentry -p {pwd} --property 'foo=line 1\\nline 2'",
        kpbig.kp,
        kpbig.ioh,
    )

    th.assert_fields_dct(
        kpbig.kp,
        "newentry",
        {"username": "", "password": pwd, "p:foo": ["line 1", "line 2"]},
    )


def test_add_many_properties(kpbig, th):
    pwd = "pwd"
    th.cmd(
        f"add newentry -p {pwd} --property foo=bar --property baz=blah",
        kpbig.kp,
        kpbig.ioh,
    )

    th.assert_fields_dct(
        kpbig.kp,
        "newentry",
        {"username": "", "password": pwd, "p:foo": ["bar"], "p:baz": ["blah"]},
    )


def test_add_property_twice(kpbig, th):
    pwd = "pwd"
    th.cmd(
        f"add newentry -p {pwd} --property foo=bar --property foo=other",
        kpbig.kp,
        kpbig.ioh,
    )

    th.assert_fields_dct(
        kpbig.kp,
        "newentry",
        {"username": "", "password": pwd, "p:foo": ["other"]},
    )


def test_add_empty_property(kpbig, th):
    pwd = "pwd"
    th.cmd(
        f"add newentry -p {pwd} --property foo=",
        kpbig.kp,
        kpbig.ioh,
    )

    fields = th.fields("newentry", kpbig.kp)
    assert "p:foo" not in fields
    assert "foo" not in fields


@pytest.mark.parametrize("prop", ["foo", "=foo", "=", "UserName=foo"])
def test_add_invalid_properties(kpbig, th, prop):
    pwd = "pwd"

    with pytest.raises(CommandError):
        th.cmd(
            f"add newentry -p {pwd} --property {prop}",
            kpbig.kp,
            kpbig.ioh,
        )

    assert "newentry" not in kpbig.kp.entries


def test_add_detect_file_modification(kpbig, th, kp_open):
    def modify_db_and_answer_password(text, is_password):
        assert is_password is True
        db = kpbig.args.db
        curr = os.stat(db)
        os.utime(db, (curr.st_atime, curr.st_mtime + 100))
        return "pwd"

    kpbig.ioh.prompt.side_effect = modify_db_and_answer_password
    th.cmd(f"add newentry", kpbig.kp, kpbig.ioh)

    assert kpbig.kp.db != kpbig.args.db
    assert os.path.exists(kpbig.args.db)
    assert os.path.exists(kpbig.kp.db)

    oldkp = kp_open(kpbig.args.db, password="foobar")
    assert th.fields("newentry", oldkp.kp) is None

    newkp_fields = th.fields("newentry", kpbig.kp)
    assert newkp_fields
    assert newkp_fields["password"] == "pwd"


def test_add_dont_add_empty_title(kpbig, th):
    with pytest.raises(CommandError):
        th.cmd(f"add group/", kpbig.kp, kpbig.ioh)
