'''
This script reads a calibration file, processes each line to find the first and last digit (considering spelled out digits), 
and then sums all the calibration values.
'''
import re
def get_digit(word):
    '''
    This function takes a word and returns its corresponding digit.
    '''
    if word == 'one':
        return '1'
    elif word == 'two':
        return '2'
    elif word == 'three':
        return '3'
    elif word == 'four':
        return '4'
    elif word == 'five':
        return '5'
    elif word == 'six':
        return '6'
    elif word == 'seven':
        return '7'
    elif word == 'eight':
        return '8'
    elif word == 'nine':
        return '9'
    else:
        return ''

# The following method was adjustes with ChatGPT-4 by one prompt. 
# https://chat.openai.com/share/f9006f4c-9639-4a8d-bfdf-b36bdbde9850
def process_line(line):
    '''
    This function processes a line from the calibration file.
    It finds the first and last digit (considering spelled out digits) and returns their combination as a two-digit number.
    '''
    digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    first_digit = ''
    last_digit = ''
    i = 0
    j = len(line) - 1

    # Function to convert digit words to their corresponding number
    def get_digit(word):
        return str(digit_words.index(word) + 1)

    # Find the first digit or digit word
    while i < len(line) and not first_digit:
        if line[i].isdigit():
            first_digit = line[i]
        else:
            for word in digit_words:
                if line[i:i+len(word)] == word:
                    first_digit = get_digit(word)
                    break
        i += 1

    # Find the last digit or digit word
    while j >= 0 and not last_digit:
        if line[j].isdigit():
            last_digit = line[j]
        else:
            for word in digit_words:
                if j >= len(word) - 1 and line[j-len(word)+1:j+1] == word:
                    last_digit = get_digit(word)
                    break
        j -= 1

    return int(first_digit + last_digit) if first_digit and last_digit else None
def main():
    '''
    This is the main function that reads the calibration file and calculates the sum of all calibration values.
    '''
    with open('calibration.txt', 'r') as file:
        lines = file.readlines()
    total = sum(process_line(line) for line in lines)
    print(f'The sum of all calibration values is {total}.')
if __name__ == '__main__':
    main()