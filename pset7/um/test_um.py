import um

def main():
    test_case()
    test_count()
    test_notum()
    
def test_case():
    assert um.count("UM HELLO") == 1
    assert um.count("THANKS, UM, SHREE, UM") == 2

def test_count():
    assert um.count("um") == 1
    assert um.count("um, thanks, um..., ") == 2
    assert um.count("um?") == 1

def test_notum():
    assert um.count("tummy") == 0
    assert um.count("umiyo") == 0
    assert um.count("mummy") == 0

if __name__ == "__main__":
    main()
