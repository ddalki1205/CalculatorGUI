''' 24 line program, remember to delete comments or atleast read in case he wants u to explain how it runs'''
from tkinter import *
from functools import partial

''' A list of tuple pairs that correspond with display and its actual value'''
button_layout = [
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

row, col, stack = 0, 0, []                                    # initializing variables for buttons and the stack used for calculations and storing data


def operate(arg):                                             # ** this function runs the operations
    if arg == '=':                                            # **first check if button is equal sign**
        result = eval(''.join([str(item) for item in stack]))   # turn every item  in the stack into a string then use eval function and set as the result
        stack.clear()                                           # remove all items in stack   
        stack.append(result)                                    # append the result as the only item in the stack(so that you can continue operating numbers on the answer)
    else:                                                     # **if the button is a number, an operation, or clear**
        stack.append(arg) if arg != 'C' else stack.clear()      # append the item if it's not the clear button else remove all items from stack

    ds = ''.join([str(item) for item in stack])               # -> ds := display string converts all items into a string so that join function can be used to turn into a string
    ''' if there was no str(item), it would cause an error if the stack had an int as .join() expects string instances'''
    result_display.config(text = ds if stack else '0')        # display the string if there is an item in a stack else just display 0


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