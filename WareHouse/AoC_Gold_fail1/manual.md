# Calibration Puzzle Solver

This application is designed to solve a unique puzzle involving calibration values. The Elves have a calibration document that has been altered by a young Elf. The document consists of lines of text, each containing a specific calibration value that needs to be recovered. The calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number. The twist is that some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

## Quick Install

This application is developed in Python. You need to have Python installed on your system to run it. You can download Python from [here](https://www.python.org/downloads/).

After installing Python, you can run the application by executing the `main.py` file.

## How to Use

The application provides a simple graphical user interface. When you run the application, you will see a window with a "Calculate" button. Click this button to calculate the sum of all calibration values.

The application reads the calibration values from a file named `calibration.txt` in the current folder. The file is very long, so if you decide to output it, only use the first 10 lines, but calculate the solution using everything.

## Main Functions

The application consists of several functions:

- `parse_line(line)`: This function takes a line of text as input and returns the first and last digit of the line. It handles both numeric and spelled out digits.

- `sum_calibration_values(lines)`: This function takes a list of lines as input and returns the sum of the calibration values of all lines.

- `read_file(filename)`: This function reads the calibration file and returns a list of lines.

The application also includes a `GUI` class that handles the graphical user interface of the program. It displays the result and provides a way for the user to interact with the program.

## Troubleshooting

If you encounter any issues while using the application, please check the following:

- Make sure you have Python installed on your system.

- Make sure the `calibration.txt` file is in the same folder as the `main.py` file.

- If you see any error messages, try to understand what they mean. They can often give you a clue about what is wrong.

If you still can't solve the problem, don't hesitate to ask for help. You can contact us at [support@chatdev.com](mailto:support@chatdev.com).