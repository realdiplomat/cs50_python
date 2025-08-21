'''
1. Expects a str in any of the 12-hour formats:-

    9:00 AM to 5:00 PM
    9 AM to 5 PM
    9:00 AM to 5 PM
    9 AM to 5:00 PM

2. Returns the corresponding str in 24-hour format
3. Expect that AM and PM will be capitalized with space before each
4. Raise a ValueError when:-

    not in either of those formats
    time is invalid (e.g., 12:60 AM, 13:00 PM, etc.)

5. Not required, to use re and/or sys.
'''


import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([0-9]{1,2}):?([0-9]{2})? (AM|PM) to ([0-9]{1,2}):?([0=9]{2})? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError

    group = match.groups()
    # [9, 30 or None, AM, 2, 30 or None, PM]

    start_h = group[0]
    start_m = group[1]
    start_ampm = group[2]
    end_h = group[3]
    end_m = group[4]
    end_ampm = group[5]

    start_h, end_h = int(start_h), int(end_h)
    start_m = int(start_m) if start_m else 0
    end_m = int(end_m) if end_m else 0

    if not (0 <= start_m < 60 and 0 <= end_m < 60):
        raise ValueError

    if not (1 <= start_h <= 12 and 1 <= end_h <= 12):
        raise ValueError


# 24HR Conversion
    #start time
    if start_ampm == "AM":
        if start_h == 12:
            start_h = 0
    else:
        if start_h != 12:
            start_h = start_h + 12
    #end time
    if end_ampm == "AM":
        if end_h == 12:
            end_h = 0
    else:
        if end_h != 12:
            end_h = end_h + 12

    return f"{start_h:02}:{start_m:02} to {end_h:02}:{end_m:02}"

if __name__ == "__main__":
    main()
