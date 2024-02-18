import ctypes
from ctypes import cdll
from ctypes import c_char_p
from json import loads
import os
import sys
dir = os.path.dirname(sys.modules["pybetterqs"].__file__)
path = os.path.join(dir, "libdor_qs.so")
pd = cdll.LoadLibrary(path)
pd.test_fn.argtypes = [c_char_p]
pd.test_fn.restype = c_char_p


def parse(input_str):
    c_input_str = ctypes.c_char_p(input_str.encode("utf-8"))
    result = pd.test_fn(c_input_str)
    result_str = ctypes.cast(result, ctypes.c_char_p).value.decode("utf-8")
    json_param = loads(result_str)
    return json_param
