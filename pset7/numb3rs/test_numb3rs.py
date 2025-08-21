import numb3rs as n

def main():
    test_true()
    test_false()

def test_true():
    assert n.validate("127.23.23.1") == True
    assert n.validate("17.213.231.0") == True
    assert n.validate("255.53.32.11") == True
    assert n.validate("233.43.10.20") == True

def test_false():
    assert n.validate("cat") == False
    assert n.validate("275.23.34.2.1") == False
    assert n.validate("512.512.512.512") == False
    assert n.validate("255.1") == False
    assert n.validate("255.1.2") == False
    assert n.validate("255.255.266.344") == False


if __name__ == "__main__":
    main()
