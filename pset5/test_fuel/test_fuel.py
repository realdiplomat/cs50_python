import fuel as f
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert f.convert("1/2") == 50
    assert f.convert("3/4") == 75
    assert f.convert("1/4") == 25
    assert f.convert("99/100") == 99

    with pytest.raises(ValueError):
        f.convert("s/i")
    with pytest.raises(ZeroDivisionError):
        f.convert("1/0")

def test_gauge():
    assert f.gauge(100) == "F"
    assert f.gauge(0.1) == "E"
    assert f.gauge(1) == "E"
    assert f.gauge(50) == "50%"
    assert f.gauge(99) == "F"

