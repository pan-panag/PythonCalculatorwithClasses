import tkinter as tk
from math import *

#Colour codes // Our Palette
purple_button = '#A94DC1'
active_purple_button = '#B458CB'
bg_black = '#22232e'
dark_button = '#474E68'
light_button = '#50577A'
active_light_button = '#5A6285'
active_dark_button = '#525973'
delete_button = '#963C71'
active_delete_button = '#A1477B'
screen_color ='#96B6C5'
screen_text_color = '#0D1D40'


class GUI():
    '''
    Creates and manages the graphical user interface.
    '''
    def __init__(self, root):
        self.screen(root)
        self.buttons(root)
        self.root.minsize(425, 500) #minimum size of window
        self.root.configure(bg=bg_black)

    def screen(self, root):
        self.root = root    #Gets the window
        root.title('Calculator')    #Changes name of window
        self.frame_screen = tk.Frame(root, background=bg_black, border= 2)  #frame for calculator screen
        self.frame_screen.pack(padx=10, pady=10, fill='x')  #padding around the screen and fills x
        self.label_screen = tk.Label(self.frame_screen, 
                            text= '', #initial text
                            font =('Courier', 20, 'bold'),    #label text format
                            foreground= screen_text_color,     #colors
                            background = screen_color, 
                            anchor= 'e',  #allignment
                            justify='right',
                            height=2 #height of label
                            )
        root.iconbitmap('icon.ico')    #change of icon
        self.label_screen.pack(fill='x')    #label screen

    def buttons(self, root):
        self.frame_buttons = tk.Frame(root, bg=bg_black)
        self.frame_buttons.pack(padx=10, pady=10, fill='both', expand=True)


        #Format dictionaries (use "**dictionary" to unpack properly)
        button_format_1={
            'font': ('Courier', 16, 'bold'),
            'background': light_button,
            'foreground': 'white',
            'activebackground': active_light_button,
            'activeforeground':'white',
            'highlightbackground':light_button,
            'border': 0
        }

        button_format_2={
            'font': ('Courier', 16, 'bold'),
            'background': dark_button,
            'foreground': 'white',
            'activebackground': active_dark_button,
            'activeforeground':'white',
            'highlightbackground':dark_button,
            'border': 0
        }
        
        button_format_purple = {
            'font': ('Courier', 16, 'bold'),
            'background': purple_button,
            'foreground': 'white',
            'activebackground': active_purple_button,
            'activeforeground':'white',
            'highlightbackground':purple_button,
            'border': 0
        }

        button_format_3={
            'font': ('Courier', 16, 'bold'),
            'background': delete_button,
            'foreground': 'white',
            'activebackground': active_delete_button,
            'activeforeground':'white',
            'highlightbackground':delete_button,
            'border': 0
        }

        grid_format ={
            'padx': 1,
            'pady': 1,
            'sticky': 'nsew'
        }


        #Column and row configuration for grid
        for c in range(6):
            self.frame_buttons.grid_columnconfigure(c, weight=1)
        for r in range(7):
            self.frame_buttons.grid_rowconfigure(r, weight=1)
        
        #Number Buttons
        self.button1 = tk.Button(self.frame_buttons, text="1", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"1"))
        self.button2 = tk.Button(self.frame_buttons, text="2", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"2"))
        self.button3 = tk.Button(self.frame_buttons, text="3", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"3"))
        self.button4 = tk.Button(self.frame_buttons, text="4", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"4"))
        self.button5 = tk.Button(self.frame_buttons, text="5", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"5"))
        self.button6 = tk.Button(self.frame_buttons, text="6", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"6"))
        self.button7 = tk.Button(self.frame_buttons, text="7", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"7"))
        self.button8 = tk.Button(self.frame_buttons, text="8", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"8"))
        self.button9 = tk.Button(self.frame_buttons, text="9", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"9"))
        self.button0 = tk.Button(self.frame_buttons, text="0", **button_format_1, command= lambda: ButtonOperations.button_operation(self,"0"))

        self.button1.grid(row=5, column=2, **grid_format)
        self.button2.grid(row=5, column=3, **grid_format)
        self.button3.grid(row=5, column=4, **grid_format)

        self.button4.grid(row=4, column=2, **grid_format)
        self.button5.grid(row=4, column=3, **grid_format)
        self.button6.grid(row=4, column=4, **grid_format)

        self.button7.grid(row=3, column=2, **grid_format)
        self.button8.grid(row=3, column=3, **grid_format)
        self.button9.grid(row=3, column=4, **grid_format)

        self.button0.grid(row=6, column=3, **grid_format)


        #OPERATORS
        #row 0
        self.button_memstore = tk.Button(self.frame_buttons, text='MS', **button_format_2, command = lambda: Memory.mem_store(self))
        self.button_memrecall = tk.Button(self.frame_buttons, text='MR', **button_format_2, command = lambda: Memory.mem_recall(self))
        self.button_memclear = tk.Button(self.frame_buttons, text='MC', **button_format_3, command = lambda: Memory.mem_clear(self))
        self.button_allclear = tk.Button(self.frame_buttons, text='AC', **button_format_3, command= lambda: ButtonOperations.all_clear_operation(self))
        self.button_backspace = tk.Button(self.frame_buttons, text='⌫', **button_format_3, command= lambda: ButtonOperations.backspace_operation(self))

        self.button_memstore.grid(row=0, column=1, **grid_format)
        self.button_memrecall.grid(row=0, column=2, **grid_format)
        self.button_memclear.grid(row=0, column=3, **grid_format)
        self.button_allclear.grid(row=0, column=4, **grid_format)
        self.button_backspace.grid(row=0, column=5, **grid_format)


        #row 1
        self.button_sin = tk.Button(self.frame_buttons, text=' sin ', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"sin("))
        self.button_cos = tk.Button(self.frame_buttons, text=' cos ', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"cos("))
        self.button_tan = tk.Button(self.frame_buttons, text=' tan ', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"tan("))
        self.button_arcsin = tk.Button(self.frame_buttons, text='sin⁻¹', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"sin⁻¹("))
        self.button_arccos = tk.Button(self.frame_buttons, text='cos⁻¹', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"cos⁻¹("))
        self.button_arctan = tk.Button(self.frame_buttons, text='tan⁻¹', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"tan⁻¹("))

        self.button_sin.grid(row=1, column=0, **grid_format)
        self.button_cos.grid(row=1, column=1, **grid_format)
        self.button_tan.grid(row=1, column=2, **grid_format)
        self.button_arcsin.grid(row=1, column=3, **grid_format)
        self.button_arccos.grid(row=1, column=4, **grid_format)
        self.button_arctan.grid(row=1, column=5, **grid_format)


        #row 2
        self.button_inverse = tk.Button(self.frame_buttons, text='1/x', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"1/"))
        self.button_modulo = tk.Button(self.frame_buttons, text='mod', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"mod"))
        self.button_parenthesis_open = tk.Button(self.frame_buttons, text='(', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"("))
        self.button_parenthesis_close = tk.Button(self.frame_buttons, text=')', **button_format_2, command= lambda: ButtonOperations.button_operation(self,")"))
        self.button_factorial = tk.Button(self.frame_buttons, text='n!', **button_format_2, command= lambda: ButtonOperations.button_operation(self, 'factorial('))
        self.button_divide = tk.Button(self.frame_buttons, text='÷', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"÷"))

        self.button_inverse.grid(row=2, column=0, **grid_format)
        self.button_modulo.grid(row=2, column=1, **grid_format)
        self.button_parenthesis_open.grid(row=2, column=2, **grid_format)
        self.button_parenthesis_close.grid(row=2, column=3, **grid_format)
        self.button_factorial.grid(row=2, column=4, **grid_format)
        self.button_divide.grid(row=2, column=5, **grid_format)


        #row 3
        self.button_absolute = tk.Button(self.frame_buttons, text='|x|', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"abs("))
        self.button_pi = tk.Button(self.frame_buttons, text='π', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"π"))
        self.button_multiply = tk.Button(self.frame_buttons, text='×', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"×"))


        self.button_absolute.grid(row=3, column=0, **grid_format)
        self.button_pi.grid(row=3, column=1, **grid_format)
        self.button_multiply.grid(row=3, column=5, **grid_format)


        #row 4
        self.button_squareroot = tk.Button(self.frame_buttons, text='√x', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"√("))
        self.button_e = tk.Button(self.frame_buttons, text='e', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"e"))
        self.button_minus = tk.Button(self.frame_buttons, text='-', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"-"))

        self.button_squareroot.grid(row=4, column=0, **grid_format)
        self.button_e.grid(row=4, column=1, **grid_format)
        self.button_minus.grid(row=4, column=5, **grid_format)


        #row 5
        self.button_exponent_y = tk.Button(self.frame_buttons, text='xʸ', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"^("))
        self.button_log = tk.Button(self.frame_buttons, text='log', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"log("))
        self.button_plus = tk.Button(self.frame_buttons, text='+', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"+"))

        self.button_exponent_y.grid(row=5, column=0, **grid_format)
        self.button_log.grid(row=5, column=1, **grid_format)
        self.button_plus.grid(row=5, column=5, **grid_format)


        #row 6
        self.button_square = tk.Button(self.frame_buttons, text='x²', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"²"))
        self.button_ln = tk.Button(self.frame_buttons, text='ln', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"ln("))
        self.button_negate = tk.Button(self.frame_buttons, text='bin', **button_format_2, command = lambda:ButtonOperations.binary(self))
        self.button_decimal_point = tk.Button(self.frame_buttons, text='.', **button_format_2, command= lambda: ButtonOperations.button_operation(self,"."))
        self.button_equals = tk.Button(self.frame_buttons, text='=', **button_format_purple, command= lambda:Calculate.evaluate(self))

        self.button_square.grid(row=6, column=0, **grid_format)
        self.button_ln.grid(row=6, column=1, **grid_format)
        self.button_negate.grid(row=6, column=2, **grid_format)
        self.button_decimal_point.grid(row=6, column=4, **grid_format)
        self.button_equals.grid(row=6, column=5, **grid_format)


        #Memory label // Not a button
        mem_label_format = {
            'font': ('Courier', 16, 'bold'),
            'background': screen_color,
            'foreground': screen_text_color,
            'highlightbackground':screen_color,
            'border': 0
        }
        self.mem_label = tk.Label(self.frame_buttons, text='', **mem_label_format )
        self.mem_label.grid(row=0, column=0, **grid_format)


        #Keybinds
        def key_pressed(event):
            key_operations = {
                "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
                "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
                "+": "+", "-": "-", "*": "×", "/": "/", "(": "(",
                ")": ")", ".": ".", "e": "e", "π": "π", "p": "π"
            }
            
            if event.char in key_operations:
                ButtonOperations.button_operation(self, key_operations[event.char])
            root.bind("<KeyPress>", key_pressed)

        
        # def key_pressed(event):
        #     if event.char=="0":
        #         ButtonOperations.button_operation(self,"0")
        #     if event.char=="1":
        #         ButtonOperations.button_operation(self,"1")
        #     if event.char=="2":
        #         ButtonOperations.button_operation(self,"2")
        #     if event.char=="3":
        #         ButtonOperations.button_operation(self,"3")
        #     if event.char=="4":
        #         ButtonOperations.button_operation(self,"4")
        #     if event.char=="5":
        #         ButtonOperations.button_operation(self,"5")
        #     if event.char=="6":
        #         ButtonOperations.button_operation(self,"6")
        #     if event.char=="7":
        #         ButtonOperations.button_operation(self,"7")
        #     if event.char=="8":
        #         ButtonOperations.button_operation(self,"8")
        #     if event.char=="9":
        #         ButtonOperations.button_operation(self,"9")
        #     if event.char=="+":
        #         ButtonOperations.button_operation(self,"+")
        #     if event.char=="-":
        #         ButtonOperations.button_operation(self,"-")
        #     if event.char=="*":
        #         ButtonOperations.button_operation(self,"×")
        #     if event.char=="/":
        #         ButtonOperations.button_operation(self,"÷")
        #     if event.char=="(":
        #         ButtonOperations.button_operation(self,"(")
        #     if event.char==")":
        #         ButtonOperations.button_operation(self,")")
        #     if event.char==".":
        #         ButtonOperations.button_operation(self,".")
        #     if event.char=="e":
        #         ButtonOperations.button_operation(self,"e")
        #     if event.char=="π" or event.char=="p":
        #         ButtonOperations.button_operation(self,"π")
        #     if event.char=="a" or event.char=="A":
        #         ButtonOperations.all_clear_operation(self)
        # root.bind("<KeyPress>", key_pressed)
        
        def backspace_pressed(event):
            if event.keysym=="BackSpace":
                ButtonOperations.backspace_operation(self)
        root.bind("<BackSpace>", backspace_pressed)

        def enter_pressed(event):
            if event.keysym=="Return":
                Calculate.evaluate(self)
        root.bind("<Return>", enter_pressed)
        
        #Trigonometric functions are bound to their first letter
        def sin_pressed(event):
            if event.keysym=="s":
                ButtonOperations.button_operation(self,"sin(")
        root.bind("<KeyPress-s>", sin_pressed)

        def cos_pressed(event):
            if event.keysym=="c":
                ButtonOperations.button_operation(self,"cos(")
        root.bind("<KeyPress-c>", cos_pressed)
        
        def tan_pressed(event):
            if event.keysym=="t":
                ButtonOperations.button_operation(self,"tan(")
        root.bind("<KeyPress-t>", tan_pressed)


class ButtonOperations():
    '''
    Contains the button-press functions.
    '''
    def __init__(self):
        self.label_screen = GUI.label_screen

    def button_operation(self, text):
        '''
        For Buttons 0-9, parentheses (), and basic operations + - × ÷, or anything text.
        '''
        
        current_text = str(self.label_screen.cget("text"))  #gets text from screen label
        if current_text == "Error": #if previous operation was invalid, replace label with empty string
            current_text = ""
        elif text == "+" or text == "-" or text == "×" or text == "÷":  #if input text is an operator and previous character also an operator, it gets replaced
            if current_text[-1] == "+" or current_text[-1] == "-" or current_text[-1] == "×" or current_text[-1] == "÷":
                current_text = current_text[:-1]
        
        new_text = current_text + text  #creates new text
        self.label_screen.configure(text = new_text)    #displays it to the screen

    def all_clear_operation(self):
        self.label_screen.configure(text='')    #AC function deletes expression
        
    def backspace_operation(self):
        current_text = str(self.label_screen.cget("text"))
        if current_text == "Error":
            new_text = ""
        else:
            new_text = current_text[:-1]    #discards last character in label text
        self.label_screen.configure(text=new_text)

    def binary(self):
        self.current_text = str(self.label_screen.cget("text"))
        try:
            self.current_text_parts = self.current_text.split('.')
            self.integer_part = int(self.current_text_parts[0])
            self.decimal_part = int(self.current_text_parts[1])
            self.binary_integer_part = bin(self.integer_part)[2:]
            self.binary_float_part = str(ButtonOperations.float_to_bin(self, self.decimal_part))
            self.binary_number = self.binary_integer_part + '.' + self.binary_float_part[2:]
        except:
            self.binary_number = bin(int(self.current_text))[2:]
        self.label_screen.configure(text = self.binary_number)
            
    def float_to_bin(self, n):
        number = '0.'
        while len(number)<10:
            n = 2*n
            if n>1:
                n = n - 1
                number += '1'
            else:
                number += '0'
        return number


class Memory():
    '''
    Manages the memory buttons and the memory element.
    '''
    memory = 0  #class-level variable for memory element

    def __init__(self):
        self.label_screen = GUI.label_screen
        self.sceen_text = self.label_screen.cget('text')
        self.mem_label = GUI.mem_label
    
    def mem_store(self):
        self.expression = str(self.label_screen.cget("text"))
        self.expression_formated = Calculate.format_screen_text(self)       
        self.output = ''
        try:
            result = eval(self.expression_formated) #performs operation
            self.output = round(result, 10)
        except:
            pass
        self.memory = self.output   #saves it to the class
        self.mem_label.configure(text="M")
    
    def mem_recall(self):
        self.new_text = str(self.label_screen.cget('text')) + str(self.output)  #new text on screen
        self.label_screen.configure(text = self.new_text)
    
    def mem_clear(self):
        self.output = ''
        self.mem_label.configure(text="")


class Calculate():
    '''
    Performs the calculation on the screen and displays the result.
    '''
    def __init__(self, label_screen):
        self.label_screen = label_screen
    
    def format_screen_text(self):
        #Includes necessary replacements in the expression string
        s = str(self.label_screen.cget("text"))
        
        #Format dictionary with all the necessary replacements
        formating = {
            " ": "",
            "^": "**",
            "²": "**2",
            "π": "pi",
            "mod": "%",
            "×": "*",
            "÷": "/",
            "sin⁻¹": "asin",
            "cos⁻¹": "acos",
            "tan⁻¹": "atan",
            "√": "sqrt",
            "log": "log10",
            "ln": "log"
        }
        
        #ke and kπ to k*e and k*π for k a float
        result = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                if i + 1 < len(s) and s[i + 1] == 'e':
                    result += s[i] + '*e'
                    i += 2
                    continue
                elif i + 1 < len(s) and s[i + 1] == 'π':
                    result += s[i] + '*π'
                    i += 2
                    continue
            result += s[i]
            i += 1
        s = result

        #Makes the replacements
        for key,value in formating.items():
            s = s.replace(key,value)
        return s
    
    def evaluate(self):
        #Makes the calculation, displays "Error" message if it is impossible
        self.expression_formated = Calculate.format_screen_text(self)       
        output = ''
        try:
            result = eval(self.expression_formated)
            
            output = round(result, 10)
        except:
            output = 'Error'
        self.label_screen.configure(text = output)
        return output


class Main():
    def __init__(self):
        root = tk.Tk()
        GUI(root)
        root.mainloop()


if __name__ == '__main__':
    calc = Main()