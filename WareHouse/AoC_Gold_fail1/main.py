'''
This is the main file of the program. It handles the main logic of the program and calls other functions.
'''
import tkinter as tk
from tkinter import messagebox
import re
import os

def parse_line(line):
    '''
    This function takes a line of text as input and returns the first and last digit of the line.
    It handles both numeric and spelled out digits.
    '''
    digit_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    line = line.lower()
    words = line.split()
    first_digit = None
    last_digit = None
    for word in words:
        if word in digit_map:
            if first_digit is None:
                first_digit = digit_map[word]
            last_digit = digit_map[word]
        else:
            for char in word:
                if char.isdigit():
                    if first_digit is None:
                        first_digit = char
                    last_digit = char
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0
def sum_calibration_values(lines):
    '''
    This function takes a list of lines as input and returns the sum of the calibration values of all lines.
    '''
    return sum(parse_line(line) for line in lines)
def read_file(filename):
    '''
    This function reads the calibration file and returns a list of lines.
    '''
    with open(filename, 'r') as file:
        return file.readlines()
    
import tkinter as tk
from tkinter import messagebox
class GUI:
    '''
    This class handles the graphical user interface of the program.
    It displays the result and provides a way for the user to interact with the program.
    '''
    def __init__(self, root):
        
        self.root = root
        self.button = tk.Button(root, text="Calculate", command=self.calculate)
        self.button.pack()
    def calculate(self):
        lines = read_file('calibration.txt')
        result = sum_calibration_values(lines)
        messagebox.showinfo("Result", f"The sum of all calibration values is {result}")
def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()