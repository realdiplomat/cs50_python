#comment not to be counted
#blank line not to be counted
#docstring NOT to be USED
    #comment like this not to be counted

import sys



def main():
    print(sys_file())

def sys_file():

    #to get the filename ending with .py
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else: #for python lines.py hello.py
        filehandle = sys.argv[1]
        #to count normal statement
        count_lines = 0
        if filehandle.endswith(".py"):
            try:
                with open(filehandle) as file:
                    for line in file:
                        #for normal statement counting via ignoring # and blank line
                        if not line.strip().startswith("#") and line.split() != []:
                            count_lines += 1

            except FileNotFoundError:
                sys.exit("File does not exist")

        else:
            sys.exit("Not a Python file")

    return count_lines

if __name__ == "__main__":
    main()
