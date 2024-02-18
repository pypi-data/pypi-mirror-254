import pytest
from unittest.mock import call


@pytest.fixture
def shared_kpbig(shared_kp_factory):
    data = shared_kp_factory("db_argon2_kdbx4_pass_big.kdbx", password="foobar")
    data.ioh.print.reset_mock()
    return data


@pytest.fixture
def kpbig(kp_factory):
    return kp_factory("db_argon2_kdbx4_pass_big.kdbx", password="foobar")


full_ls = [
    call("foo"),
    call("group/entry"),
    call("group/subgroup/entry"),
    call("group/subgroup/other entry"),
    call("other/foo"),
]

group_ls = [
    call("group/entry"),
    call("group/subgroup/entry"),
    call("group/subgroup/other entry"),
]


@pytest.mark.parametrize(
    "glob,expected_prints",
    [
        ("", full_ls),
        ("*", full_ls),
        ("foo", [call("foo")]),
        ("foobar", []),
        ("f*", [call("foo")]),
        ("group/*", group_ls),
        ("group", group_ls),
        ("group/", group_ls),
    ],
)
def test_ls(shared_kpbig, glob, expected_prints, th):
    th.cmd(f"ls {glob}", shared_kpbig.kp, shared_kpbig.ioh)
    shared_kpbig.ioh.print.assert_has_calls(expected_prints)


def test_show(shared_kpbig, th):
    th.cmd("show foo", shared_kpbig.kp, shared_kpbig.ioh)
    shared_kpbig.ioh.print.assert_has_calls(
        [
            call("path: foo"),
            call("username: myuser"),
            call("password: mypass"),
            call("url: http://example.com"),
            call("autotype_sequence: {USER}{PASSWORD}"),
            call("notes[1]: first note"),
            call("notes[2]: second note"),
            # properties
            call("p:param 1[1]: first line"),
            call("p:param 1[2]: second line"),
            call("p:param 2[1]: value"),
            call("p:username[1]: example"),
        ]
    )


def test_show_n(shared_kpbig, th):
    th.cmd("show foo -n", shared_kpbig.kp, shared_kpbig.ioh)
    shared_kpbig.ioh.print.assert_has_calls(
        [
            call("foo"),
            call("myuser"),
            call("mypass"),
            call("http://example.com"),
            call("{USER}{PASSWORD}"),
            call("first note"),
            call("second note"),
            # properties
            call("first line"),
            call("second line"),
            call("value"),
            call("example"),
        ]
    )


@pytest.mark.parametrize(
    "field,lines",
    [
        ("path", ["foo"]),
        ("username", ["myuser"]),
        ("password", ["mypass"]),
        ("url", ["http://example.com"]),
        ("autotype_sequence", ["{USER}{PASSWORD}"]),
        ("notes", ["first note", "second note"]),
    ],
)
def test_show_field(shared_kpbig, field, lines, th):
    th.cmd(f"show foo {field}", shared_kpbig.kp, shared_kpbig.ioh)
    expected_calls = (
        [call(f"{field}: {lines[0]}")]
        if len(lines) == 1
        else [call(f"{field}[{i+1}]: {line}") for i, line in enumerate(lines)]
    )
    shared_kpbig.ioh.print.assert_has_calls(expected_calls)

    shared_kpbig.ioh.print.reset_mock()
    th.cmd(f"show -n foo {field}", shared_kpbig.kp, shared_kpbig.ioh)
    expected_calls = [call(line) for line in lines]
    shared_kpbig.ioh.print.assert_has_calls(expected_calls)


def test_show_many_fields_different_order(shared_kpbig, th):
    th.cmd(f"show foo url path", shared_kpbig.kp, shared_kpbig.ioh)
    shared_kpbig.ioh.print.assert_has_calls(
        [call("url: http://example.com"), call("path: foo")]
    )


@pytest.mark.parametrize(
    "key,prints",
    [
        (
            "param 1",
            [call("p:param 1[1]: first line"), call("p:param 1[2]: second line")],
        ),
        ("param 2", [call("p:param 2[1]: value")]),
        (
            "p:param 1",
            [call("p:param 1[1]: first line"), call("p:param 1[2]: second line")],
        ),
        ("p:param 2", [call("p:param 2[1]: value")]),
        # ordinary field
        ("username", [call("username: myuser")]),
        # property with the same name as field
        (
            "p:username",
            [call("p:username[1]: example")],
        ),
    ],
)
def test_show_properties(shared_kpbig, th, key, prints):
    shared_kpbig.ioh.print.reset_mock()
    th.cmd(f"show foo '{key}'", shared_kpbig.kp, shared_kpbig.ioh)
    shared_kpbig.ioh.print.assert_has_calls(prints)


@pytest.mark.parametrize(
    "key,prints",
    [
        ("param 1", [call("first line"), call("second line")]),
        ("p:param 1", [call("first line"), call("second line")]),
        ("username", [call("myuser")]),  # ordinary field
        ("p:username", [call("example")]),  # property with the same name as field
    ],
)
def test_show_properties_n(shared_kpbig, th, key, prints):
    shared_kpbig.ioh.print.reset_mock()
    th.cmd(f"show -n foo '{key}'", shared_kpbig.kp, shared_kpbig.ioh)
    shared_kpbig.ioh.print.assert_has_calls(prints)


def test_db(kpbig, th):
    th.cmd("db", kpbig.kp, kpbig.ioh)
    kpbig.ioh.print.assert_has_calls([call(kpbig.args.db), call("Locked: True")])

    kpbig.ioh.print.reset_mock()
    th.cmd("unlock", kpbig.kp, kpbig.ioh)


def test_echo(shared_kpbig, th):
    msg = "foo bar baz"
    th.cmd(f"echo '{msg}'", shared_kpbig.kp, shared_kpbig.ioh)
    shared_kpbig.ioh.print.assert_has_calls([call(msg)])
