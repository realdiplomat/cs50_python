def main():
    x = input("Enter a string: ")
    convert(x)

def convert(n):
    if ":)" or ":(" in n:
        print(n.replace(":)","🙂").replace(":(", "🙁"))

main()


