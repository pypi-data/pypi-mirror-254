import pytest


@pytest.fixture
def kpbig(kp_factory):
    return kp_factory("db_argon2_kdbx4_pass_big.kdbx", password="foobar")


def test_delete(kpbig, th):
    expected = kpbig.kp.entries.copy()
    del expected["foo"]

    assert "foo" in kpbig.kp.entries
    th.cmd("delete foo", kpbig.kp, kpbig.ioh)
    assert kpbig.kp.entries == expected


def test_dont_delete_missing_entry(kpbig, th):
    expected = kpbig.kp.entries.copy()

    th.cmd(f"delete somethingwhichdoesntexist", kpbig.kp, kpbig.ioh)
    assert kpbig.kp.entries == expected


def test_delete_entry_in_subgroup(kpbig, th):
    expected = kpbig.kp.entries.copy()
    del expected["other/foo"]

    th.cmd("delete other/foo", kpbig.kp, kpbig.ioh)
    assert kpbig.kp.entries == expected


def test_delete_many(kpbig, th):
    expected = kpbig.kp.entries.copy()
    del expected["foo"]
    del expected["other/foo"]
    del expected["group/subgroup/other entry"]

    th.cmd("delete foo other/foo 'group/subgroup/other entry'", kpbig.kp, kpbig.ioh)
    assert kpbig.kp.entries == expected


def test_delete_group_recursively(kpbig, th):
    expected_entries = {
        key: val
        for key, val in kpbig.kp.entries.copy().items()
        if not key.startswith("group/")
    }
    expected_groups = [g for g in kpbig.kp.groups[:] if not g.startswith("group")]

    assert "group" in kpbig.kp.groups

    th.cmd("delete group --recursive", kpbig.kp, kpbig.ioh)
    assert kpbig.kp.groups == expected_groups
    assert kpbig.kp.entries == expected_entries


def test_delete_group_no_recursive_flag(kpbig, th):
    expected_entries = kpbig.kp.entries.copy()
    expected_groups = kpbig.kp.groups[:]

    th.cmd("delete group", kpbig.kp, kpbig.ioh)
    assert kpbig.kp.groups == expected_groups
    assert kpbig.kp.entries == expected_entries
    assert kpbig.ioh.eprint.has_calls()


def test_delete_many_group_no_recursive_flag(kpbig, th):
    expected_entries = kpbig.kp.entries.copy()
    del expected_entries["foo"]
    del expected_entries["other/foo"]
    expected_groups = kpbig.kp.groups[:]

    th.cmd("delete foo group other/foo", kpbig.kp, kpbig.ioh)
    assert kpbig.kp.groups == expected_groups
    assert kpbig.kp.entries == expected_entries
    assert kpbig.ioh.eprint.has_calls()


def test_delete_group_twice(kpbig, th):
    expected_entries = {
        key: val
        for key, val in kpbig.kp.entries.copy().items()
        if not key.startswith("group/")
    }
    expected_groups = [g for g in kpbig.kp.groups[:] if not g.startswith("group")]

    th.cmd("delete group group/subgroup --recursive", kpbig.kp, kpbig.ioh)
    assert kpbig.kp.groups == expected_groups
    assert kpbig.kp.entries == expected_entries
    assert kpbig.ioh.eprint.has_calls()


@pytest.mark.parametrize("title", ["group", "group/subgroup"])
def test_delete_entry_with_the_same_name_as_group(kpbig, th, title):
    # First, let's add a new entry with the same name as found group
    th.cmd(f"add '{title}' --password foo", kpbig.kp, kpbig.ioh)
    assert title in kpbig.kp.entries
    assert title in kpbig.kp.groups

    th.cmd(f"delete '{title}'", kpbig.kp, kpbig.ioh)
    assert title not in kpbig.kp.entries
    assert title in kpbig.kp.groups
