import os
import string

import pytest

from kpsh.commands import CommandError


@pytest.fixture
def kpbig(kp_factory):
    return kp_factory("db_argon2_kdbx4_pass_big.kdbx", password="foobar")


@pytest.fixture
def shared_kpbig(shared_kp_factory):
    data = shared_kp_factory("db_argon2_kdbx4_pass_big.kdbx", password="foobar")
    data.ioh.print.reset_mock()
    return data


def test_edit_nothing(kpbig, th):
    expected = th.fields("foo", kpbig.kp).copy()
    th.cmd("edit foo", kpbig.kp, kpbig.ioh)
    assert th.fields("foo", kpbig.kp) == expected


@pytest.mark.parametrize(
    "field,switch,value",
    [
        ("username", "--username", "editeduser"),
        ("password", "--password", "editedpassword"),
        ("url", "--url", "editeturl"),
        ("autotype_sequence", "--autotype-sequence", "{TAB}{TAB}{TAB}"),
    ],
)
def test_edit_fields(kpbig, th, field, switch, value):
    expected = th.fields("foo", kpbig.kp).copy()
    assert expected[field] != value
    expected[field] = value

    th.cmd(f"edit foo {switch} {value}", kpbig.kp, kpbig.ioh)
    assert th.fields("foo", kpbig.kp) == expected


@pytest.mark.parametrize(
    "path", ["foo", "group/entry", "'group/subgroup/other entry'", "other/foo"]
)
def test_edit_fields_paths(kpbig, th, path):
    expected = th.fields(path, kpbig.kp).copy()
    expected["url"] = "newurl"

    th.cmd(f"edit {path} -U newurl", kpbig.kp, kpbig.ioh)
    assert th.fields(path, kpbig.kp) == expected


def test_edit_many_fields(kpbig, th):
    expected = th.fields("foo", kpbig.kp).copy()
    expected["username"] = "euser"
    expected["url"] = "eurl"
    expected["password"] = "epwd"

    th.cmd("edit foo -p epwd -U eurl -u euser ", kpbig.kp, kpbig.ioh)
    assert th.fields("foo", kpbig.kp) == expected


@pytest.mark.parametrize("password", ["editedpassword", ""])
def test_edit_password_interactively(kpbig, th, password):
    expected = th.fields("foo", kpbig.kp).copy()
    expected["password"] = password
    kpbig.ioh.prompt.return_value = password

    th.cmd("edit foo --askpass", kpbig.kp, kpbig.ioh)
    assert th.fields("foo", kpbig.kp) == expected


@pytest.mark.parametrize(
    "field,switch",
    [
        ("username", "--username"),
        ("password", "--password"),
        ("url", "--url"),
        ("autotype_sequence", "--autotype-sequence"),
    ],
)
def test_edit_unset_fields(kpbig, th, field, switch):
    assert field in th.fields("foo", kpbig.kp)
    th.cmd(f"edit foo {switch} ''", kpbig.kp, kpbig.ioh)
    assert not th.fields("foo", kpbig.kp).get(field)


def test_edit_generate_password(kpbig, th):
    th.cmd(f"edit foo --generate-password-no-confirm -l 32", kpbig.kp, kpbig.ioh)
    fields = th.fields("foo", kpbig.kp)
    assert len(fields["password"]) == 32


@pytest.mark.parametrize(
    "arg,chset",
    [
        ("--letters", string.ascii_letters),
        ("--digits", string.digits),
        ("--punctuation", string.punctuation),
        ("--logograms", "#$%&@^`~"),
        ("--characters abc", "abc"),
    ],
)
def test_edit_generate_password_character_sets(kpbig, th, arg, chset):
    th.cmd(f"edit foo --generate-password-no-confirm -l 100 {arg}", kpbig.kp, kpbig.ioh)

    fields = th.fields("foo", kpbig.kp)
    assert len(fields["password"]) == 100

    for ch in fields["password"]:
        assert (
            ch in chset
        ), f"'{ch}' is in set of letters allowed for generated password"


def test_edit_generate_password_interactively(kpbig, th):
    old_password = kpbig.kp.entries["foo"].password
    kpbig.ioh.prompt.side_effect = ["n", "a"]
    th.cmd(f"edit foo --generate-password -l 100", kpbig.kp, kpbig.ioh)

    assert len(kpbig.ioh.print.call_args_list) == 2
    assert len(kpbig.ioh.prompt.call_args_list) == 2
    fields = th.fields("foo", kpbig.kp)
    assert fields
    assert len(fields["password"]) == 100
    assert fields["password"] != old_password


def test_add_generate_password_interactively_cancel(kpbig, th):
    old_fields = th.fields("foo", kpbig.kp).copy()

    kpbig.ioh.prompt.return_value = "c"
    th.cmd(f"edit foo --generate-password -l 100", kpbig.kp, kpbig.ioh)
    assert th.fields("foo", kpbig.kp) == old_fields


def test_edit_add_notes(kpbig, th):
    existing = th.fields("foo", kpbig.kp)["notes"]

    th.cmd("edit foo --note 'note 1'", kpbig.kp, kpbig.ioh)
    expected = existing + ["note 1"]
    assert th.fields("foo", kpbig.kp)["notes"] == expected

    th.cmd("edit foo --note 'note 2' --note 'note 3'", kpbig.kp, kpbig.ioh)
    expected = existing + ["note 1", "note 2", "note 3"]
    assert th.fields("foo", kpbig.kp)["notes"] == expected


@pytest.mark.parametrize(
    "pattern,expected",
    [
        ("1", ["2", "3", "4", "5"]),
        ("2", ["1", "3", "4", "5"]),
        ("5", ["1", "2", "3", "4"]),
        ("6", ["1", "2", "3", "4", "5"]),
        ("2-3", ["1", "4", "5"]),
        ("2-6", ["1"]),
    ],
)
def test_delete_notes(kpbig, th, pattern, expected):
    th.cmd("add tabula_rasa -p pwd -n1 -n2 -n3 -n4 -n5", kpbig.kp, kpbig.ioh)
    th.cmd(f"edit tabula_rasa --delete-note {pattern}", kpbig.kp, kpbig.ioh)
    assert th.fields("tabula_rasa", kpbig.kp)["notes"] == expected


@pytest.mark.parametrize("pattern", ["*", "1-5", "1-6"])
def test_delete_all_notes(kpbig, th, pattern):
    th.cmd("add tabula_rasa -p pwd -n1 -n2 -n3 -n4 -n5", kpbig.kp, kpbig.ioh)
    th.cmd(f"edit tabula_rasa --delete-note {pattern}", kpbig.kp, kpbig.ioh)
    assert "notes" not in th.fields("tabula_rasa", kpbig.kp)


@pytest.mark.parametrize(
    "pattern", ["0", "a", "0-1", "1-", "-", "-0", "-1", ",", "**", "1*"]
)
def test_delete_notes_incorrect_argument(shared_kpbig, th, pattern):
    th.cmd("edit foo -n1 -n2 -n3 -n4 -n5", shared_kpbig.kp, shared_kpbig.ioh)
    expected = th.fields("foo", shared_kpbig.kp).copy()

    cmd = f"edit foo --delete-note {pattern}"
    with pytest.raises(CommandError):
        th.cmd(cmd, shared_kpbig.kp, shared_kpbig.ioh)

    assert th.fields("foo", shared_kpbig.kp) == expected


def test_edit_add_delete_together(kpbig, th):
    existing = th.fields("foo", kpbig.kp)["notes"]
    assert existing

    th.cmd("edit foo -N * -n 'note 1'", kpbig.kp, kpbig.ioh)
    expected = ["note 1"]
    assert th.fields("foo", kpbig.kp)["notes"] == expected


def test_edit_detect_file_modification(kpbig, th, kp_open):
    def modify_db_and_answer_password(text, is_password):
        assert is_password is True
        db = kpbig.args.db
        curr = os.stat(db)
        os.utime(db, (curr.st_atime, curr.st_mtime + 100))
        return "pwd"

    expected_unchanged = th.fields("foo", kpbig.kp).copy()

    kpbig.ioh.prompt.side_effect = modify_db_and_answer_password
    th.cmd(f"edit foo --askpass", kpbig.kp, kpbig.ioh)

    assert kpbig.kp.db != kpbig.args.db
    assert os.path.exists(kpbig.args.db)
    assert os.path.exists(kpbig.kp.db)

    oldkp = kp_open(kpbig.args.db, password="foobar")
    assert th.fields("foo", oldkp.kp) == expected_unchanged

    newkp_fields = th.fields("foo", kpbig.kp)
    assert newkp_fields
    assert newkp_fields["password"] == "pwd"


@pytest.mark.parametrize("path", ["'missing path'", "missing", "foo/missing"])
def test_edit_not_existing_path(shared_kpbig, th, path):
    assert path not in shared_kpbig.kp.entries
    with pytest.raises(CommandError):
        th.cmd(f"edit {path} -p pwd", shared_kpbig.kp, shared_kpbig.ioh)


@pytest.mark.parametrize(
    "name,value",
    [
        ("foo", "bar"),
        ("username", "baz"),
        ("param 1", "baz"),
        ("param 2", "baz"),
    ],
)
def test_edit_property(kpbig, th, name, value):
    pname = f"p:{name}"
    expected = th.fields("foo", kpbig.kp).copy()
    expected[pname] = [value]

    pwd = "pwd"
    th.cmd(
        f"edit foo --property '{name}={value}'",
        kpbig.kp,
        kpbig.ioh,
    )

    assert th.fields("foo", kpbig.kp) == expected


def test_edit_multiline_property(kpbig, th):
    expected = th.fields("foo", kpbig.kp).copy()
    expected["p:foo"] = ["line 1", "line 2"]

    pwd = "pwd"
    th.cmd(
        "edit foo --property 'foo=line 1\\nline 2'",
        kpbig.kp,
        kpbig.ioh,
    )

    assert th.fields("foo", kpbig.kp) == expected


def test_edit_property_twice(kpbig, th):
    expected = th.fields("foo", kpbig.kp).copy()
    expected["p:foo"] = ["other"]

    pwd = "pwd"
    th.cmd(
        "edit foo --property foo=bar --property foo=other",
        kpbig.kp,
        kpbig.ioh,
    )

    assert th.fields("foo", kpbig.kp) == expected


@pytest.mark.parametrize("name", ["not existing", "username", "param 1"])
def test_edit_delete_property(kpbig, th, name):
    pname = f"p:{name}"
    expected = th.fields("foo", kpbig.kp).copy()
    expected.pop(pname, None)

    pwd = "pwd"
    th.cmd(
        f"edit foo --property '{name}='",
        kpbig.kp,
        kpbig.ioh,
    )

    assert th.fields("foo", kpbig.kp) == expected


@pytest.mark.parametrize("prop", ["foo", "=foo", "=", "UserName=foo"])
def test_edit_invalid_property(kpbig, th, prop):
    with pytest.raises(CommandError):
        th.cmd(
            f"edit foo --property {prop}",
            kpbig.kp,
            kpbig.ioh,
        )


def test_edit_error_fully_reverts(kpbig, th):
    oldfields = th.fields("foo", kpbig.kp).copy()

    with pytest.raises(CommandError):
        th.cmd(
            f"edit foo --username newname --property UserName=foo",
            kpbig.kp,
            kpbig.ioh,
        )

    assert oldfields == th.fields("foo", kpbig.kp)


def test_edit_saves_history(kpbig, th):
    assert not kpbig.kp.entries["foo"].history
    old_username = kpbig.kp.entries["foo"].username

    th.cmd("edit foo -u someusername", kpbig.kp, kpbig.ioh)

    history = kpbig.kp.entries["foo"].history[-1]
    assert history.username == old_username


def test_empty_edit_doesnt_change_history(kpbig, th):
    # pykeepass has weird handling of empty notes, which can be either None or
    # an empty string. That's why, contrary to other tests, we select here
    # an entry without any notes
    assert not kpbig.kp.entries["other/foo"].history
    assert kpbig.kp.entries["other/foo"].notes is None  # sanity check

    th.cmd("edit other/foo", kpbig.kp, kpbig.ioh)
    assert not kpbig.kp.entries["other/foo"].history
    assert kpbig.kp.entries["other/foo"].notes is None  # sanity check

    th.cmd("edit other/foo -N *", kpbig.kp, kpbig.ioh)
    assert not kpbig.kp.entries["other/foo"].history
    assert kpbig.kp.entries["other/foo"].notes is None  # sanity check
