import twttr as t

#MISTAKE: only main should print the function
#MISTAKE: return value must be INT not string

def main():
    test_twttr()

def test_twttr():

        assert t.shorten("TWITTER") == "TWTTR"

        assert t.shorten("What's your name?") == "Wht's yr nm?"

        assert t.shorten("CS50") == "CS50"

        assert t.shorten("123") == "123"




if __name__ == "__main__":
    main()
