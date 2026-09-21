from plates import is_valid

def test_short_plate():
    assert is_valid("1") == False

def test_long_plate():
    assert is_valid("AA345678") == False

def test_symbols_plate():
    assert is_valid("$%^&*#$%^") == False

def test_correct_plate():
    assert is_valid("AAA123") == True

def test_wrong_order():
    assert is_valid("12AAAA") == False

def test_no_alpha():
    assert is_valid("AAAAAA") == True
