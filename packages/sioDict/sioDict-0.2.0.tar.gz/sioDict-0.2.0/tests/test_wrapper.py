import os 
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sioDict.wrapper import SioWrapper

def test_wrapper():
    w = SioWrapper("test.json")
    # {"hello":{"world":[null,3]}}
    w["hello", "world", 1] = 3