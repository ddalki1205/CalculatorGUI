from tkinter import *
from functools import partial
layout = [('x^a', '**'), ('|÷|', '//'), ('%', '%'), ('C', 'C'), 
          ('7', 7), ('8', 8), ('9', 9), ('÷', '/'), 
          ('4', 4), ('5', 5), ('6', 6), ('*', '*'), 
          ('1', 1), ('2', 2), ('3', 3), ('+', '+'), 
          ('.', '.'), ('0', 0), ('=', '='), ('-', '-')]
win = Tk()
win.geometry(f"{280}x{386}+600+250")
win.config(bg = "#000000")
result_display = Label(win, height = 2, text = '0', font = ("Century Gothic", 20), bg = "#000000", fg = "#FFFFFF")
result_display.grid(row = 0, column = 0, columnspan = 4)
row, col, stack = 0, 0, []
def cmd(arg):
    if arg == '=':
        result = eval(''.join([str(item) for item in stack]))
        stack.clear()
        stack.append(result) if result != 0 else print("encountered a zero as the result, not appending result.")
    else:
        stack.append(arg) if arg != 'C' else stack.clear()
    ds = ''.join([str(item) for item in stack])
    result_display.config(text = ds if stack else '0')
for (dv, av) in layout:
    Button(win, width = 5, height = 2,
            command = partial(cmd, av), 
            border = 0,
            text = dv, font = ("Century Gothic", 15), fg = 'white', bg = '#505050' if isinstance(av, int) or dv in '=.' else '#acacac' if dv != 'C' else '#FF9500').grid(row = row + 1, column = col)
    row = (row + 1) if col == 3 else row
    col = (col + 1) if col != 3 else 0
win.title("My Calculator") 
win.mainloop()