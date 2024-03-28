# PythonCalculatorwithClasses
Calculator App with Classes
    Version: v1.0.0
	Language:	Python v3.12.0
	Modules used:	tkinter, math



Installation guide:
	1. Extract the .zip file
	No further steps are required

For users:
	Run the file named "calculator.exe". The program should launch.
	Do not move it from the parent folder.
	Click the buttons on the window, or tap keys on keyboard to input expression to calculate.
		-Use the numpad or the number keyboard on the GUI to type numbers <0-9> and basis operators <+,-,*,/>.
        -Use parentheses, decimal point to type those into the display frame.
        -For exponents, type the base and then the exponent.
        -Memory is single value. <MS> is memory set, <MR> is memory recall and <MC> is memory clear.
        -Backspace deletes the last character on the screen. May break functions.
        -AC clears the expression, not the memory.
        -Type a number, or calculate an expression and then click <bin> to convert to binary. 
		-Click or tap <=> on the keyboard to get result.
        -The format for the mod function is "x mod y".

        
    Keyboard integration:
        -Tapping the <0-9> keys on your keyboard, or your numpad inputs the respective number.
        -Tapping <e> inputs e.
        -Tapping <p> inputs π.
        -Tapping open/closed parenthesis inputs that.
        -<s> inputs sine function.
        -<c> inputs cosine function.
        -<t> inputs tangent function.

**NOTICES**
-Most functions open a parenthesis automatically. Those need to be closed by the user.
-The Calculator works with rounding at 10 digits.
-The file with all the code is included in the .zip folder, named "calculator.py". The file calc_icon.ico is required to run.
-The program is not optimised to handle very large numbers. Trying to perform calculations with large digits may result in unexpected errors.
