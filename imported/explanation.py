''' 24 line program, remember to delete comments or atleast read in case he wants u to explain how it runs'''
from tkinter import *
from functools import partial

''' A list of tuple pairs that correspond with display and its actual value'''
button_layout: list[tuple] = [
    ('x^a', '**'), ('|÷|', '//'), ('%', '%'), ('C', 'C'),
    ('7', 7), ('8', 8), ('9', 9), ('÷', '/'),
    ('4', 4), ('5', 5), ('6', 6), ('*', '*'),
    ('1', 1), ('2', 2), ('3', 3), ('+', '+'),
    ('.', '.'), ('0', 0), ('=', '='), ('-', '-')
]

''' Setting up the window's config here '''
root = Tk()
root.geometry(f"{280}x{386}+600+250")
root.config(bg = "#000000")
result_display = Label(
    master = root,
    height = 2,
    text = '0',
    font = ("Century Gothic", 20),
    bg = "#000000",
    fg = "#FFFFFF"

)
result_display.grid(row = 0, column = 0, columnspan = 4)      # column span determines the width of the label

row, col = 0, 0                                    # initializing variables for buttons and the stack used for calculations and storing data

def operate(arg):
    '''current display := 
        get the text of display and check if the first letter is 0, if it is...
        splice the string to remove the 0 by getting the next letter'''
    current_display = str(result_display.cget('text')) if str(result_display.cget('text'))[0] != '0' else str(result_display.cget('text'))[1:]
    if arg == '=':
        result_display.config(text = eval(current_display))     # evaluate the string and show the result
    elif arg == 'C':
        result_display.config(text = '0')                       # set the result equal to 0
    else:
        current_display += str(arg)                             # add the new input from the button onto the current text in the dispay
        result_display.config(text = current_display)


for (display, value) in button_layout: #creating a button from the list of tuples. dv := display value, av := actual value
    Button(
        master = root, 
        width = 5, height = 2, 
        command = partial(operate, value), 
        text = display, 
        font = ("Century Gothic", 15), 
        fg = 'white', 
        bg = '#505050' if isinstance(value, int) or value in '=.' else '#acacac' if value != 'C' else '#FF9500').grid(row = row + 1, column = col)
    row = (row + 1) if col == 3 else row    # short way of going to the next row if the last button added was on the last row, else just stay as the same value
    col = (col + 1) if col != 3 else 0      # keep going right until you've hit the max row then go back to 0


root.mainloop()