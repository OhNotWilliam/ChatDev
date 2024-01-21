# Calibration Puzzle Solver

This Python application is designed to solve a unique puzzle involving calibration values. It reads a calibration document and calculates the sum of all calibration values. The calibration value of each line is determined by combining the first and last digit (in that order) to form a single two-digit number. Digits can be actual numbers or spelled out with letters: one, two, three, four, five, six, seven, eight, and nine.

## Quick Install

Ensure that you have Python 3.8 or higher installed on your machine. You can download it from the official Python website.

## How to Use

1. Save the Python script (`main.py`) in a directory of your choice.

2. Save the calibration document (`calibration.txt`) in the same directory as the Python script.

3. Open a terminal window and navigate to the directory where you saved the Python script.

4. Run the script by typing `python main.py` and pressing Enter.

The script will read the calibration document, calculate the calibration value of each line, and print the sum of all calibration values.

## Functionality

The application includes the following functions:

- `get_digit(word)`: This function takes a word and returns its numerical equivalent if it's a spelled out digit. If the word is not a spelled out digit, it returns the word itself.

- `get_calibration_value(line)`: This function takes a line of text and returns its calibration value. The calibration value is determined by combining the first and last digit (in that order) to form a single two-digit number.

- `get_total_calibration_value(filename)`: This function takes a filename, reads the file line by line, calculates the calibration value of each line, and returns the sum of all calibration values.

## Edge Cases

The application is designed to handle a variety of edge cases. For example, it can handle lines that contain no digits, lines that contain only one digit, and lines that contain multiple digits. It can also handle lines that contain spelled out digits in addition to or instead of actual digits.

## Support

If you encounter any issues while using this application, please open an issue on our GitHub repository. We will do our best to resolve it as quickly as possible.