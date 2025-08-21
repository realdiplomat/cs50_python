import working as w
import pytest

def main():
    test_time()
    test_invalid_format()
    test_invalid_hour()
    test_invalid_min()

def test_time():
    assert w.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert w.convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert w.convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert w.convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        w.convert("9 AM 5 PM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        w.convert("21 AM to 5 PM")

def test_invalid_min():
    with pytest.raises(ValueError):
        w.convert("9:61 AM to 5:61 PM")

if __name__ == "__main__":
    main()
