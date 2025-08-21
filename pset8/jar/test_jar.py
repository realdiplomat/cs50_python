from jar import Jar
import pytest

def test_init():
    jar1 = Jar()

    assert jar1.capacity == 12
    with pytest.raises(ValueError):
        jar2 = Jar(capacity = -1)


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar_dep = Jar(capacity = 10)
    jar_dep.deposit(5)

    assert jar_dep.size == 5
    with pytest.raises(ValueError):
        jar_dep.deposit(8)

def test_withdraw():
    jar_with = Jar(capacity = 10)
    jar_with.deposit(8)
    jar_with.withdraw(5)
    
    assert jar_with.size == 3
    with pytest.raises(ValueError):
        jar_with.deposit(8)


