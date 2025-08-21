from random import randint as R

#10 probs
#3 errors
#display score

def main():
    score = 0
    prob_no = 0

    level = get_level()

    while prob_no < 10:
        error = 0
        if error == 0:
            x = generate_integer(level)
            y = generate_integer(level)
            answer = x+y

            while error < 3:
                try:
                    problem = int(input(f"{x} + {y} = "))

                    if problem == answer:
                        score += 1
                        break
                    else:
                        print("EEE")
                        error += 1
                except ValueError:
                    print("EEE")
                    error += 1

            if error == 3:
                print(f"{x} + {y} = {answer}")
            prob_no += 1

    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
                continue
        except ValueError:
            print("Enter level 1, 2 or 3 !")

def generate_integer(level):
    if level == 1:
        return R(0,9)

    elif level == 2:
        return R(10,99)

    elif level == 3:
        return R(100,999)

if __name__ == "__main__":
    main()
