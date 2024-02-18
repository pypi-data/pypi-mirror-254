from unittest.mock import Mock, call
import pytest

from kpsh.cleanup import cleanup


def test_run():
    fn = Mock()
    c = cleanup(fn)
    c()
    fn.assert_called_once()


def test_run_exception():
    fn = Mock(side_effect=RuntimeError("foo"))
    c = cleanup(fn)
    with pytest.raises(RuntimeError):
        c()


def test_run_args_kwargs():
    fn = Mock()
    c = cleanup(fn, 1, 2, foo="bar")
    c()
    fn.assert_called_with(1, 2, foo="bar")


def test_cancel():
    fn = Mock()
    c = cleanup(fn, 1, 2, foo="bar")
    c.cancel()
    c()
    fn.assert_not_called()


def test_run_all():
    fn1 = Mock()
    fn2 = Mock()
    fn3 = Mock()

    cleanup(fn1)
    cleanup(fn2).cancel()
    cleanup(fn3)

    cleanup.run_all()

    fn1.assert_called_once()
    fn2.assert_not_called()
    fn3.assert_called_once()


def test_clean_on_exit():
    fn1 = Mock()
    fn2 = Mock()
    fn3 = Mock()

    cleanup(fn1)
    cleanup(fn2).cancel()
    cleanup(fn3)

    with cleanup.clean_on_exit():
        fn1.assert_not_called()
        fn2.assert_not_called()
        fn3.assert_not_called()

    fn1.assert_called_once()
    fn2.assert_not_called()
    fn3.assert_called_once()


def test_run_all_exception(capsys):
    fn1 = Mock()
    fn2 = Mock(side_effect=RuntimeError("foo error"))
    fn3 = Mock()

    cleanup(fn1)
    cleanup(fn2)
    cleanup(fn3)

    cleanup.run_all()

    fn1.assert_called_once()
    fn2.assert_called_once()
    fn3.assert_called_once()

    err = capsys.readouterr().err
    assert "foo error" in err


def test_run_all_order():
    m = Mock()

    cleanup(m.f1)
    cleanup(m.f2)
    cleanup(m.f3)

    cleanup.run_all()
    m.assert_has_calls([call.f3, call.f2, call.f1])
