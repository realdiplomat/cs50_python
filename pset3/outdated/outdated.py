#input = month-date-year or September 8, 1636
#output = year-month-date

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date: #12/11/1900
            month, day, year = date.split("/")


        elif "," in date: # September 9, 1834
            date = date.replace("," , "")
            month, day, year = date.split(" ")

            if month in months:
                month = months.index(month) + 1
        else:
            continue

        if int(month) > 12 or int(day) > 31:
            continue
        else:
            break

    except ValueError:
        continue


print(f"{int(year)}-{int(month):02}-{int(day):02}")
