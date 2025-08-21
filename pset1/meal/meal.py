'''
1. formatted in 24-hour time
2. bfast - between 7:00 and 8:00
3. lunch - between 12:00 and 13:00
4. dinner - between 18:00 and 19:00
'''

def main():
    x = input("Whats the time?: ")
    time = convert(x)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    h,m = time.split(":")
    return float(h) + float(m)/60


if __name__ == "__main__":
    main()
