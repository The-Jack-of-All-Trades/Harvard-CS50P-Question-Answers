from bank import value

def test_symbols():
    assert value("hiya folks!!!") == "$20"

def test_nums():
    assert value("1234hello") == "$100"

def test_nothing():
    assert value("") == "$100"

def test_hello():
    assert value("hello there") == "$0"
