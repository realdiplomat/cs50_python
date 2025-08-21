import re
import sys

#   #.#.#.#. where # = 0 - 255
#   Return True for eg: 255.255.255.0
#   Return False for eg: 275.1.2.4

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    try:
        pattern = r"^([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)$"

        match = re.search(pattern, ip)

        m1 = int(match.group(1))
        m2 = int(match.group(2))
        m3 = int(match.group(3))
        m4 = int(match.group(4))

        if m1 <= 255 and m2 <= 255 and m3 <= 255 and m4 <= 255:
            return True
        else:
            return False

    except AttributeError:
        return False

if __name__ == "__main__":
    main()
