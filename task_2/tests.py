from hack_loyalty_programm import calculate
from pytest import mark
from test_data import *

@mark.parametrize("m,n,p,expected", test_data)
def test_analyse(m, n, p, expected):
    assert calculate(m, n, p) == expected
    
