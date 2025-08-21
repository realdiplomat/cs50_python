while True:
    try:
        fraction = input("Fraction: ")
        x,y=fraction.split("/")

        int_x=int(x)
        int_y=int(y)

        int_fraction = int_x/int_y
        if int_fraction <=1:
            break
# for x>y

# for x,y not int
    except ValueError:
        pass
# for y (denominator) as 0
    except ZeroDivisionError:
        pass

percent = int_fraction*100

if percent <= 1:
    print("E")
elif percent >=99:
    print("F")
else:
    print(f"{round(percent)}%")


