import plates as p

def main():
    test_start()
    test_middle()
    test_zero()
    test_splchar()
    test_length()
    test_nplacement()

def test_length():
    assert p.is_valid("HELLO") == True
    assert p.is_valid("C") == False

def test_nplacement():
    assert p.is_valid("TELL56") == True
    assert p.is_valid("AA12B") == False

def test_start():
    assert p.is_valid("AA") == True
    assert p.is_valid("A1") == False
    assert p.is_valid("11") == False
    assert p.is_valid("1A") == False

def test_middle():
    assert p.is_valid("AAA123") == True
    assert p.is_valid("A1A") == False

def test_zero():
    assert p.is_valid("AA12") == True
    assert p.is_valid("AA01") == False

def test_splchar():
    assert p.is_valid("AA..AA") == False
    assert p.is_valid("A1??A") == False

if __name__ == "__main__":
    main()
