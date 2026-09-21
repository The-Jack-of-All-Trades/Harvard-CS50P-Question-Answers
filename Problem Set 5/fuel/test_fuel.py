from cs50p import convert, gauge
import pytest

def test_negative():
    with pytest.raises(ValueError):
        convert(["-1", "4"])

def test_x_greater():
    with pytest.raises(ValueError):
        convert(["100", "3"])

def test_correct_convert():
    assert convert(["3", "4"]) == 75

def test_empty():
    assert gauge(0.0001) == "E"

def test_full():
    assert gauge(99.9) == "F"

def test_large():
    with pytest.raises(ValueError):
        gauge(1000)

def test_correct_gauge():
    assert gauge(45) == "45%"
