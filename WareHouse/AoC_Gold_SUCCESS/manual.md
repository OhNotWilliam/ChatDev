# Calibration Value Calculator

This Python application helps to recover calibration values from a document that has been altered. The calibration values are found by combining the first and last digit (in that order) on each line to form a single two-digit number. The application also handles cases where digits are spelled out with letters: one, two, three, four, five, six, seven, eight, and nine.

## Quick Install

This application does not require any special installation. It only requires Python 3.x to be installed on your machine.

## How to Use

1. Save the Python script (`main.py`) in a directory on your machine.

2. Save the calibration document (`calibration.txt`) in the same directory.

3. Open a terminal and navigate to the directory containing the script and the calibration document.

4. Run the script with the command `python main.py`.

The application will read the calibration document, process each line to find the first and last digit (considering spelled out digits), and then sum all the calibration values. The sum of all calibration values will be printed to the terminal.

## Functions

- `get_digit(word)`: This function takes a word and returns its corresponding digit.

- `process_line(line)`: This function processes a line from the calibration file. It finds the first and last digit (considering spelled out digits) and returns their combination as a two-digit number.

- `main()`: This is the main function that reads the calibration file and calculates the sum of all calibration values.

## Edge Cases

The application handles several edge cases:

- Lines with mixed words and digits: The application correctly identifies the first and last digit even when they are mixed with words.

- Lines with words that could be parsed as two numbers at once: The application correctly identifies the first and last digit even when they are part of a word that could be parsed as two numbers (e.g., "oneight").

- Lines with only one digit at the end: The application correctly identifies the first and last digit even when there is only one digit at the end of the line.

- Lines with no digits: The application correctly handles lines with no digits by skipping them.

## Note

This application does not create a GUI. It is designed to be run from the command line.