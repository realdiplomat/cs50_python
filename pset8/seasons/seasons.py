'''
1. date of birth in YYYY-MM-DD format
2. how old they are in minutes, rounded to the nearest integer
3. English words instead of numerals
4. without any and between words
5. user was born at midnight
'''

# VALID - YYYY - MM - DD

from datetime import date
import sys
import inflect

p = inflect.engine()


class Date:
    def __init__(self, dob):
        self.dob = dob
        self.todaydate = date.today()

    @staticmethod
    def getbirthdate():
        dob = input("Enter DOB: ")
        try:
            dob = date.fromisoformat(dob)
            return Date(dob)
        except ValueError:
            sys.exit("Invalid date")

    def numtoword(self):
        day_alive = (self.todaydate-self.dob).days
        minute_alive = day_alive*24*60
        min_word = p.number_to_words(minute_alive, andword="")
        return f"{min_word.capitalize()} minutes"

def main():
    myDob = Date.getbirthdate()
    result = myDob.numtoword()
    print(result)

if __name__ == "__main__":
    main()
