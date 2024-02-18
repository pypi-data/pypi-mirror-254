import pytest
from unittest.mock import Mock, PropertyMock

from kpsh.completion import CommandCompleter, quote
from kpsh.commands import prepare_command_parser


DEFAULT_PATHS = sorted(["foo", "bar", "baz/blah", "a b/c d", "aa/bb"])


def groups(entries, slash=False):
    groups = []
    for e in entries:
        group, _, _ = e.rpartition("/")
        if group:
            if slash:
                group += "/"
            groups.append(group)
    return groups


def quoted(iterable):
    return [quote(elem) for elem in iterable]


@pytest.fixture
def compl():
    class Fixture:
        def __init__(self):
            self.kp = Mock()

            type(self.kp).locked = PropertyMock(return_value=False)
            self.set_paths(DEFAULT_PATHS)

            _, parsers = prepare_command_parser()
            self.commands = [p for p in parsers if p]

            self.document = Mock()
            self.set_text("")

            self.completer = CommandCompleter(self.kp, self.commands)

        def set_text(self, text):
            type(self.document).text_before_cursor = PropertyMock(return_value=text)

        def lock_database(self):
            type(self.kp).locked = PropertyMock(return_value=True)

        def set_paths(self, paths):
            type(self.kp).paths = PropertyMock(return_value=paths)
            type(self.kp).groups = PropertyMock(return_value=groups(paths))

        def get_completions(self):
            return self.completer.get_completions(self.document, None)

    return Fixture()


def assert_completions(expected):
    def _check(iterable):
        completions = list(iterable)
        assert len(completions) == len(expected)

        for i, exp in enumerate(expected):
            assert exp == completions[i].text

    return _check


def assert_unordered_completions(expected):
    def _check(iterable):
        completions = sorted(iterable, key=lambda c: c.text)
        assert len(completions) == len(expected)

        for i, exp in enumerate(sorted(expected)):
            assert exp == completions[i].text

    return _check


def assert_all_long_opts(iterable):
    completions = list(iterable)
    assert len(completions) > 0
    for compl in completions:
        assert compl.text.startswith("--")


def assert_no_completions(iterable):
    completions = list(iterable)
    assert len(completions) == 0


def test_commands(compl):
    _, parsers = prepare_command_parser()
    expected = sorted(p for p in parsers if p)
    assert_completions(expected)(compl.get_completions())


@pytest.mark.parametrize(
    "text,assert_fn",
    [
        ("show ", assert_completions(quoted(DEFAULT_PATHS))),
        ("show b", assert_completions(quoted(["bar", "baz/blah"]))),
        ("show -", assert_all_long_opts),
        ("autotype ", assert_completions(quoted(DEFAULT_PATHS))),
        ("autotype -", assert_all_long_opts),
        ("add ", assert_completions(quoted(groups(DEFAULT_PATHS, slash=True)))),
        ("add a", assert_completions(quoted(["a b/", "aa/"]))),
        ("add -", assert_all_long_opts),
        ("add foo -", assert_all_long_opts),
        ("add -u foo ", assert_completions(quoted(groups(DEFAULT_PATHS, slash=True)))),
        ("edit ", assert_completions(quoted(DEFAULT_PATHS))),
        ("edit -", assert_all_long_opts),
        (
            "delete ",
            assert_completions(
                quoted(sorted(DEFAULT_PATHS + groups(DEFAULT_PATHS, slash=True)))
            ),
        ),
        ("delete -", assert_all_long_opts),
        ("move ", assert_completions(quoted(DEFAULT_PATHS))),
        ("move b", assert_completions(quoted(["bar", "baz/blah"]))),
        ("move 'b", assert_completions(quoted(["bar", "baz/blah"]))),
        ("move 'b'", assert_completions(quoted(["bar", "baz/blah"]))),
        ('move "b"', assert_completions(quoted(["bar", "baz/blah"]))),
        ("move b a", assert_completions(quoted(["a b", "aa"]))),
        ("move b 'a", assert_completions(quoted(["a b", "aa"]))),
        ("move foo ", assert_completions(quoted(groups(DEFAULT_PATHS)))),
        ("move foo newentry", assert_no_completions),
        ("move foo aa/newentry", assert_no_completions),
        ("move foo aa ", assert_no_completions),
        ("move foo aa f", assert_no_completions),
        ("move -", assert_no_completions),
    ],
)
def test_subcommands(compl, text, assert_fn):
    compl.set_text(text)
    completions = compl.get_completions()
    assert_fn(completions)


def test_help(compl):
    compl.set_text("help ")
    _, parsers = prepare_command_parser()
    expected = sorted(p for p in parsers if p)
    assert_completions(expected)(compl.get_completions())


def test_open(compl, tmpdir):
    subdir = tmpdir / "sub"
    subdir.mkdir()

    final = subdir / "final"
    final.mkdir()

    other = subdir / "other"
    other.mkdir()

    f = subdir / "file"
    f.write_text("hello world", encoding="ascii")

    compl.set_text(f"open {str(subdir)}/")
    expected = [final, other, f]
    assert_unordered_completions(expected)(compl.get_completions())


def test_ls(compl):
    compl.set_text("ls ")
    expected = quoted(groups(DEFAULT_PATHS))
    assert_completions(expected)(compl.get_completions())
