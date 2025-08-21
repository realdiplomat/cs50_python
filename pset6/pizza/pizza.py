import sys
import csv
import tabulate as tab
#use grid format

def main():
    print(sys_pizza())

def sys_pizza():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else: #for python pizza.py sicillian.csv
        filehandle = sys.argv[1]
        if filehandle.endswith(".csv"):
            try:
                with open(filehandle, "r") as file:
                    reader = csv.reader(file)
                    table = []
                    for row in reader:
                        table.append(row)
                        tabformat = tab.tabulate(table, headers="firstrow", tablefmt="grid")
                    return tabformat

            except FileNotFoundError:
                sys.exit("Not a CSV file")
                
        else:
            sys.exit("Not a CSV file")





if __name__ == "__main__":
    main()
