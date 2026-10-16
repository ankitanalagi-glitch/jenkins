from simple_interest import simpleInt

def test_simple_interest():
    assert simpleInt(1000, 5, 2) == 100

def test_zero_principal():
    assert simpleInt(0, 5, 2) == 0

def test_zero_time():
    assert simpleInt(1000, 5, 0) == 0

def test_different_values():
    assert simpleInt(2000, 10, 3) == 600