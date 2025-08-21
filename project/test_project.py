import project as p
import pytest

def main():

    test_add()
    test_sub()
    test_mult()
    test_div()
    test_avg()

def test_add():
    assert p.addition([10.0, 3.0, 2.0]) == "Resultant of [10.0, 3.0, 2.0] = 15.0"
    assert p.addition([1.0, 3.0, 2.0]) == "Resultant of [1.0, 3.0, 2.0] = 6.0"
    assert p.addition([0.0, 0.0, 0.0]) == "Resultant of [0.0, 0.0, 0.0] = 0.0"

def test_sub():
    assert p.subtraction([10.0, 3.0, 2.0]) == "Resultant of [10.0, 3.0, 2.0] = 5.0"
    assert p.subtraction([100.0, 50.0, 25.0]) == "Resultant of [100.0, 50.0, 25.0] = 25.0"
    assert p.subtraction([-1.0, -1.0, 0.0]) == "Resultant of [-1.0, -1.0, 0.0] = 0.0"
    assert p.subtraction([0.0, 0.0, 0.0]) == "Resultant of [0.0, 0.0, 0.0] = 0.0"


def test_mult():
    assert p.multiplication([10.0, 3.0, 2.0]) == "Resultant of [10.0, 3.0, 2.0] = 60.0"
    assert p.multiplication([0.0, 0.0, 0.0]) == "Resultant of [0.0, 0.0, 0.0] = 0.0"
    assert p.multiplication([100.0, 50.0, 25.0]) == "Resultant of [100.0, 50.0, 25.0] = 125000.0"

def test_div():
    assert p.division([1.0, 2.0]) == "Resultant of [1.0, 2.0] = 0.5"
    assert p.division([2.0, 1.0]) == "Resultant of [2.0, 1.0] = 2.0"
    assert p.division([1.0, 0.0]) == "Number cannot be divided by zero!"
    assert p.division([0.0, 0.0, 0.0]) == "Number cannot be divided by zero!"

def test_avg():
    assert p.average([10.0, 3.0, 2.0]) == "Resultant of [10.0, 3.0, 2.0] = 5.0"
    assert p.average([0.0, 0.0, 0.0]) == "Resultant of [0.0, 0.0, 0.0] = 0.0"
    assert p.average([10.0, 10.0, 5.0]) == "Resultant of [10.0, 10.0, 5.0] = 12.5"


if __name__ == "__main__":
    main()
