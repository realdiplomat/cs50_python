# Simple Calculator
#### Video Demo:  [Demo Video](https://youtu.be/-VsMMzxMLFI)

## Overview

The Simple Calculator is a user-friendly, command-line Python program created for the CS50P final project. It lets you perform basic math operations like addition, subtraction, multiplication, division, and finding the average of numbers. The program has a clear menu, handles errors smoothly, and uses the `tabulate` library to display options in a neat table. It also comes with a test suite to ensure everything works correctly.

## Features

- **Interactive Menu**: Displays a formatted table of operation choices using the `tabulate` library.
- **Addition**: Add multiple numbers together.
- **Subtraction**: Subtract numbers step-by-step, starting with the first number.
- **Multiplication**: Multiply multiple numbers.
- **Division**: Divide numbers in sequence, with protection against dividing by zero.
- **Average**: Calculate the average of a set of numbers.
- **Exit**: Close the program easily.
- The program checks for valid inputs and shows results in a clear format.

## Installation

- Python 3 (any recent version works).
- The `tabulate` library for the nice menu display.
- The `pytest` library to run the tests.
- The `sys` library to terminate the program.

## How to Set It Up

1. Download or clone the project files to your computer.
2. Make sure Python 3 is installed.
3. Install and import the `tabulate`, `pytest` and `sys` libraries.
4. You're ready to go! no extra setup needed!

## Usage

1. Run the program by executing the main script:
   ```
   python calculator.py
   ```
2. The program displays a menu with six options:
   ```
   +----------+----------------+
   | Choice   | Operation      |
   +==========+================+
   | 1        | Addition       |
   | 2        | Subtraction    |
   | 3        | Multiplication |
   | 4        | Division       |
   | 5        | Average        |
   | 6        | Exit           |
   +----------+----------------+
   ```
3. Select an operation by entering a number (1-6).
4. For operations 1-5, input numbers one by one. Enter 'S' to stop entering numbers and perform the calculation.
5. The program displays the result and exits after performing the selected operation, or exits directly if choice 6 is selected.
6. Example interaction:
   ```
   Calculator Program

   +-----------+---------------+
   | Choice   | Operation      |
   +==========+================+
   | 1        | Addition       |
   | 2        | Subtraction    |
   | 3        | Multiplication |
   | 4        | Division       |
   | 5        | Average        |
   | 6        | Exit           |
   +----------+----------------+

   Select your choice: 1
   Choice 1 has been used...

   Enter a number or press S to stop taking numbers: 5

   Enter a number or press S to stop taking numbers: 10

   Enter a number or press S to stop taking numbers: S

   Resultant of [5.0, 10.0] = 15.0
   ```
## Testing the Program

The project includes tests to make sure everything works. To run them:

1. Type `pytest test_project.py` in your terminal.
2. The tests check:
   1. Addition with different numbers.
   2. Subtraction with positive, negative, and zero values.
   3. Multiplication, including zeros.
   4. Division, including error cases like dividing by zero.
3. Average for various number sets.

## Files

- `project.py`: The main calculator program.
- `test_project.py`: The test suite to check the program's functions.
- `requirements.txt`: The file containing requirements of the program.

## Notes
- The program handles invalid inputs , such as non-numeric inputs or division by zero.
- Subtraction starts with the first number and subtracts subsequent numbers.
- Division starts with the first number and divides by subsequent numbers.
- The program exits after performing one operation or when the user selects the "Exit" option.

## Author

Created as part of the CS50P (Introduction to Programming with Python) final project.

## License

This project is for educational purposes and is not licensed for commercial use.


