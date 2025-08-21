def main():

    while True:

        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            per = gauge(percentage)
            print(per)
            break

        except (ValueError,ZeroDivisionError):
            pass

def convert(fraction): # frac --> percent

    x,y=fraction.split("/")

    int_x=int(x)
    int_y=int(y)

    percent = int_x/int_y

    if percent >1:
        main()
    else:
        percent = percent*100
        percent = round(percent)
        return percent


def gauge(percentage): #output generation

    if percentage <=1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
