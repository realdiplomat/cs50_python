import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):

    import re

def parse(s):

    pattern = r'<iframe[^>]*src="https?://(www\.)?youtube\.com/embed/([^"]+)"'
    match = re.search(pattern, s)
    if match:
        embed = match.group(2)
        return f"https://youtu.be/{embed}"
    return None

if __name__ == "__main__":
    main()
