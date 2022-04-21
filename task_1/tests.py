from automated_storehouse import analyse
from pytest import mark
from test_data import *

@mark.parametrize("test_programm,expected", test_data)
def test_analyse(test_programm, expected):
    assert analyse(test_programm) == expected
    
