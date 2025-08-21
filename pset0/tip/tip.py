def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    no_d = d.lstrip("$")
    return float(no_d)

def percent_to_float(p):
    no_p = p.rstrip("%")
    return float(no_p)/100

main()
