#MISTAKE: only main should print the function
#MISTAKE: return value must be INT not string

def main():
    global greet
    greet = input("Greeting: ").strip().lower()
    print(f"${value(greet)}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and greeting != "hello" :
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
