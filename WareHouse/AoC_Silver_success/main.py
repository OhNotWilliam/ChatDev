'''
This is the main file for the calibration value calculation program.
It reads the calibration document, calculates the calibration values for each line,
and then sums them up to get the total calibration value.
'''
import re
def calculate_calibration_value(line):
    '''
    This function calculates the calibration value for a given line of text.
    It does this by finding the first and last digit in the line, and combining them to form a two-digit number.
    If no digits are found in the line, it returns 0.
    '''
    digits = re.findall('\d', line)
    if len(digits) == 0:
        return 0
    else:
        return int(digits[0] + digits[-1])
def main():
    '''
    This is the main function of the program.
    It opens the calibration document, reads each line, calculates the calibration value for that line,
    and then adds it to a running total.
    Once all lines have been read, it prints out the total calibration value.
    '''
    total_calibration_value = 0
    with open('calibration.txt', 'r') as file:
        for line in file:
            total_calibration_value += calculate_calibration_value(line)
    print('The total calibration value is:', total_calibration_value)
if __name__ == "__main__":
    main()