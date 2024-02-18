from unittest.mock import Mock, PropertyMock, call

import pytest

from kpsh.entry import EntryProxy


ORDINARY_FIELDS = ["password", "username", "title", "url", "autotype_sequence"]
ALL_FIELDS = ORDINARY_FIELDS + ["notes"]


@pytest.fixture
def proxy():
    e = Mock()
    return EntryProxy(e)


@pytest.mark.parametrize("field", ORDINARY_FIELDS)
@pytest.mark.parametrize("fieldval", [None, "bar"])
def test_forward_value_of_entry(proxy, field, fieldval):
    p = PropertyMock(return_value=fieldval)
    setattr(type(proxy.realentry), field, p)
    assert getattr(proxy, field) == fieldval


@pytest.mark.parametrize("field", ORDINARY_FIELDS)
def test_set_field_of_entry(proxy, field):
    p = PropertyMock(return_value=None)
    setattr(type(proxy.realentry), field, p)

    setattr(proxy, field, "foobar")
    p.assert_called_with("foobar")
    p.return_value = "fooobar"

    setattr(proxy, field, "")
    p.assert_called_with("")


@pytest.mark.parametrize("field", ALL_FIELDS)
def test_suppress_field_update(proxy, field):
    p = PropertyMock(return_value="foo")
    setattr(type(proxy.realentry), field, p)

    setattr(proxy, field, "foo")
    assert call("foo") not in p.mock_calls

    setattr(proxy, field, None)
    assert call(None) not in p.mock_calls

    # when field wasn't set, EntryProxy should suppress its reset via empty
    # string
    p.return_value = None
    setattr(proxy, field, "")
    assert call("") not in p.mock_calls

    assert not proxy.modified


def test_get_notes(proxy):
    p = PropertyMock()
    type(proxy.realentry).notes = p

    p.return_value = ""
    assert proxy.notes == []

    p.return_value = "foo"
    assert proxy.notes == ["foo"]

    p.return_value = "foo\nbar"
    assert proxy.notes == ["foo", "bar"]


def test_set_notes(proxy):
    p = PropertyMock()
    type(proxy.realentry).notes = p

    p.reset_mock()
    proxy.notes = []
    p.assert_called_with("")

    p.reset_mock()
    proxy.notes = ["foo"]
    p.assert_called_with("foo")

    p.reset_mock()
    proxy.notes = ["foo", "bar"]
    p.assert_called_with("foo\nbar")

    p.reset_mock(return_value="foo")
    proxy.notes = None
    assert call(None) not in p.mock_calls
    assert call("None") not in p.mock_calls
    assert call("") not in p.mock_calls

    p.reset_mock(return_value="foo")
    proxy.notes = ""
    p.assert_called_with("")

    p.reset_mock(return_value="foo")
    proxy.notes = "bar"
    p.assert_called_with("bar")

    p.reset_mock(return_value="foo")
    proxy.notes = "foo\nbar"
    p.assert_called_with("foo\nbar")


def test_get_custom_property(proxy):
    proxy.realentry.get_custom_property = Mock(return_value="retval")
    assert "retval" == proxy.get_custom_property("foo")
    proxy.realentry.get_custom_property.assert_called_with("foo")


def test_set_custom_property(proxy):
    proxy.realentry.get_custom_property = Mock(return_value="retval")
    proxy.set_custom_property("prop", "bar")
    proxy.realentry.set_custom_property.assert_called_with("prop", "bar")


def test_set_custom_property_suppress_update(proxy):
    proxy.realentry.get_custom_property = Mock(return_value="foo")

    proxy.set_custom_property("prop", "foo")
    proxy.realentry.set_custom_property.assert_not_called()

    proxy.set_custom_property("prop", None)
    proxy.realentry.set_custom_property.assert_not_called()

    # when property wasn't set, EntryProxy should suppress its reset via empty
    # string
    proxy.realentry.get_custom_property.return_value = None
    proxy.set_custom_property("prop", "")
    proxy.realentry.set_custom_property.assert_not_called()

    assert not proxy.modified


def test_modified_getters(proxy):
    proxy.realentry.get_custom_property = Mock(return_value="retval")

    p = PropertyMock(return_value="foo")
    for field in ALL_FIELDS:
        setattr(type(proxy.realentry), field, p)

    proxy.get_custom_property("foo")
    for field in ALL_FIELDS:
        getattr(proxy, field)

    assert not proxy.modified


@pytest.mark.parametrize("field", ORDINARY_FIELDS)
def test_modified_fields(proxy, field):
    p = PropertyMock(return_value="foo")
    setattr(type(proxy.realentry), field, p)

    assert not proxy.modified
    setattr(proxy, field, "foobar")
    assert proxy.modified


def test_modified_property(proxy):
    proxy.realentry.get_custom_property = Mock(return_value="retval")
    assert not proxy.modified
    proxy.set_custom_property("prop", "bar")
    assert proxy.modified
