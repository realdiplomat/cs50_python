import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    count = 0

    #\b --> word bounded
    pattern = r"\bum\b"
    match_um = re.findall(pattern , s, re.IGNORECASE)
    for i in match_um:
        if match_um:
            count += 1
    return count

if __name__ == "__main__":
    main()
