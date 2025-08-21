import bank as b

#MISTAKE: return value must be INT not string
#MISTAKE: only main should print the function

def main():
     test_0()
     test_20()
     test_100()

def test_0():
    assert b.value("hello") == 0
    assert b.value("HELLO") == 0

def test_20():
    assert b.value("hey") == 20
    assert b.value("howdy") == 20

def test_100():
    assert b.value("What") == 100
    assert b.value("Yo") == 100

if __name__ == "__main__":
    main()
