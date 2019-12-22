#%load unittests.py

import re
from nose.tools import eq_,ok_,assert_equal,assert_in,assert_equal,assert_not_equal,assert_regex
import sys, io, contextlib

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
