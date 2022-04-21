from automated_storehouse import analyse
from pytest import mark

ADD = 'принять'
OUT = 'выгрузить'

sets = [
    ([(ADD, 46), (OUT, 46), (ADD, 21), (OUT, 21)], 4),
    ([(ADD, 1), (ADD, 2), (OUT, 1), (ADD, 3), (ADD, 4), (OUT, 3)], 6),
    ([(ADD, 1), (ADD, 2), (ADD, 3), (OUT, 1), (ADD, 4), (ADD, 5), 
        (ADD, 6), (OUT, 4), (OUT, 5), (OUT, 3), (OUT, 2), (ADD, 7), (ADD, 8), (OUT, 7)], 18),
    ([(ADD, 1), (ADD, 2), (ADD, 3), (ADD, 4), (ADD, 5), (ADD, 6), 
        (ADD, 7), (ADD, 8), (ADD, 9), (OUT, 6), (OUT, 3), (OUT, 1), (OUT, 2), (OUT, 7)], 18),
    ([(ADD, 1), (ADD, 2), (ADD, 3), (ADD, 4), (OUT, 1), (ADD, 5), (ADD, 6), 
        (ADD, 7), (ADD, 8), (ADD, 9), (OUT, 6), (OUT, 3), (OUT, 2), (OUT, 7)], 20),
    ([(ADD, 1), (ADD, 2), (ADD, 3), (ADD, 4), (ADD, 5), (OUT, 4), (OUT, 1), (OUT, 5), (OUT, 3), (OUT, 2)], 16)
]

@mark.parametrize("test_programm,expected", sets)
def test_analyse(test_programm, expected):
    assert analyse(test_programm) == expected
    
