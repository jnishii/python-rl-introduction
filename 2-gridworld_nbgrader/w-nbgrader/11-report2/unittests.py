# このセルは自動評価を行うための命令です。内容は無視して，実行(Shift-Enter)のみをしてください。
import re
from nose.tools import (
    eq_,
    ok_,
    assert_almost_equal,
    assert_count_equal,
    assert_equal,
    assert_in,
    assert_is,
    assert_not_equal,
    assert_regex,
)
import sys, io, contextlib
import numpy.testing as nt


class Data(object):
    pass


@contextlib.contextmanager
def capture_stdout():
    old = sys.stdout
    capturer = io.StringIO()
    data = Data()
    try:
        sys.stdout = capturer
        yield data
    finally:
        sys.stdout = old
        data.result = capturer.getvalue()


from plotchecker import LinePlotChecker, PlotChecker
