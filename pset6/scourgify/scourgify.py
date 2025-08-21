#2 CL arg: existing csv and new csv
#to change lname, fname --> fname, lname and write it to a new file containin: first, last, house

import sys
import csv

def main():
    sys_scourgify()

def sys_scourgify():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    #for python scourgify.py before.csv after.cs
    else:
        try:
            file_before = sys.argv[1]
            file_after = sys.argv[2]
        except FileNotFoundError:
            sys.exit("Could not read", sys.argv[1])

    ogfile = []

    with open(file_before, "r") as bfile:
            reader = csv.DictReader(bfile)
            for line in reader:
                lname, fname = line["name"].split(",")
                house = line["house"]
                ogfile.append({
                    "first" : fname.strip(),
                    "last" : lname.strip(),
                    "house" : house
                    })
                # strip used to remove whitespaces

    with open(file_after, "w") as afile:
        writer = csv.DictWriter(afile, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        for row in ogfile:
            writer.writerow(row)


if __name__ == "__main__":
    main()
