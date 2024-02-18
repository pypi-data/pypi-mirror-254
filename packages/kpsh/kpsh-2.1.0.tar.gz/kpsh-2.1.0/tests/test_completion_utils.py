import pytest

from kpsh.completion import Word, get_words, unquote, quote, CommandCompleter


def _words(*args):
    return [Word(i, txt, False) for i, txt in enumerate(args)]


@pytest.mark.parametrize(
    "text,expected",
    [
        ("""""", []),
        (""" """, []),
        ("""'""", [Word(0, "'", True)]),
        ("""' """, [Word(0, "' ", True)]),
        ("""foo bar""", _words("foo", "bar")),
        ("""foo\\ bar""", _words("foo bar")),
        ("""foo bar """, _words("foo", "bar")),
        ("""foo 'bar'""", _words("foo", "bar")),
        ("""foo 'bar' """, _words("foo", "bar")),
        ("""foo 'bar baz'""", _words("foo", "bar baz")),
        ("""foo 'bar baz' """, _words("foo", "bar baz")),
        ("""foo 'bar baz' blah""", _words("foo", "bar baz", "blah")),
        ("""foo 'bar""", [Word(0, "foo", False), Word(1, "'bar", True)]),
        ("""foo 'bar """, [Word(0, "foo", False), Word(1, "'bar ", True)]),
    ],
)
def test_get_words(text, expected):
    words = list(get_words(text))
    assert words == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", ""),
        ("foo", "foo"),
        ("'foo'", "foo"),
        ('"foo"', "foo"),
        ("'foo bar'", "foo bar"),
        ("'foo\\ bar'", "foo bar"),
    ],
)
def test_unquote(text, expected):
    assert expected == unquote(text)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("foo", "foo"),
        ("'foo'", "'foo'"),
        ("foo bar", "'foo bar'"),
        ("'foo bar'", "'foo bar'"),
        ('"foo bar"', """'"foo bar"'"""),
    ],
)
def test_quote(text, expected):
    assert expected == quote(text)
