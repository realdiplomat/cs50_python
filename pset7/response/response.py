import validators as v

def main():
    email = validator(input("What's your email address? "))
    print(email)

def validator(s):
    if v.email(s):
        return f"Valid"
    else:
        return f"Invalid"

if __name__ == "__main__":
    main()
