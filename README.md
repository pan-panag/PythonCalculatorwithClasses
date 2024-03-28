# Python Calculator with Classes

This repository contains a Python calculator application implemented using classes.

## Overview
- **Version:** v1.0.0
- **Language:** Python v3.12.0
- **Modules used:** tkinter, math

## Installation Guide:
1. Clone or download the repository.
2. No further installation steps are required.

## Usage:
- Run the file named "calculator.exe". The program should launch.
- Do not move it from the parent folder.
- Click the buttons on the window or use the keyboard to input expressions to calculate.
    - Use the numpad or the number keyboard on the GUI to type numbers (0-9) and basic operators (+, -, *, /).
    - Use parentheses, decimal points to type those into the display frame.
    - For exponents, type the base and then the exponent.
    - Memory is a single value. "MS" is memory set, "MR" is memory recall, and "MC" is memory clear.
    - Backspace deletes the last character on the screen. It may break functions.
    - AC clears the expression, not the memory.
    - Type a number or calculate an expression and then click "bin" to convert to binary.
    - Click or tap "<=>" on the keyboard to get the result.
    - The format for the mod function is "x mod y".

## Keyboard Integration:
- Typing the 0-9 keys on your keyboard or your numpad inputs the respective number.
- Typing "e" inputs e.
- Typing "p" inputs π.
- Typing open/closed parenthesis inputs that.
- Typing "s" inputs the sine function.
- Typing "c" inputs the cosine function.
- Typing "t" inputs the tangent function.

## Notices:
1. Most functions open a parenthesis automatically. These need to be closed by the user.
2. The calculator works with rounding at 10 digits.
3. The program is not optimized to handle very large numbers. Trying to perform calculations with large digits may result in unexpected errors.
