'''
This script reads a calibration document and calculates the sum of all calibration values. 
The calibration value of each line is determined by combining the first and last digit (in that order) to form a single two-digit number.
Digits can be actual numbers or spelled out with letters: one, two, three, four, five, six, seven, eight, and nine.
'''
import re
def get_digit(word):
    '''
    This function takes a word and returns its numerical equivalent if it's a spelled out digit. 
    If the word is not a spelled out digit, it returns the word itself.
    '''
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for spelled_digit, digit in digits.items():
        if spelled_digit in word:
            word = word.replace(spelled_digit, digit)
    return word
def get_calibration_value(line):
    '''
    This function takes a line of text and returns its calibration value.
    The calibration value is determined by combining the first and last digit (in that order) to form a single two-digit number.
    '''
    words = re.findall(r'\b\w+\b', line)
    first_digit = get_digit(words[0]) or words[0][0]
    last_digit = get_digit(words[-1]) or words[-1][-1]
    return int(first_digit + last_digit)
def get_total_calibration_value(filename):
    '''
    This function takes a filename, reads the file line by line, calculates the calibration value of each line, 
    and returns the sum of all calibration values.
    '''
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += get_calibration_value(line)
    return total
if __name__ == "__main__":
    print(get_total_calibration_value("calibration.txt"))