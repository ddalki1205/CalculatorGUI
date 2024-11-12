from tkinter import *; from functools import partial
win = Tk()
win.title("Calculator") 
win.geometry(f"344x502+{(win.winfo_screenwidth() - 344)//2}+{(win.winfo_screenheight() - 502)//2}")
win.config(bg = "#FEF3E2")
result_display = Label(win, height = 2, width = 16, text = '0', font = ("Myriad", 25, 'bold'), bg = "#FEF3E2", fg = "black")
result_display.grid(row = 0, column = 0, columnspan = 4)
row, col, stack = 0, 0, []
layout = [('^', '**'), ('|÷|', '//'), ('%', '%'), ('C', 'C'), ('7', 7), ('8', 8), ('9', 9), ('÷', '/'), ('4', 4), ('5', 5), ('6', 6), ('*', '*'), ('1', 1), ('2', 2), ('3', 3), ('-', '-'), ('.', '.'), ('0', 0), ('=', '='), ('+', '+')]
def cmd(arg):
    if arg == '=':
        try: 
            result = eval(''.join([str(item) for item in stack]))
            stack.clear()
            stack.append(result) if result != 0 else print("encountered a zero as the result, not appending.")
        except:
            stack.clear()
            result_display.config(text="Math Error")
            return
    else:
        stack.append(arg) if arg != 'C' else stack.clear()
    ds = ''.join([str(item) for item in stack])
    result_display.config(text = ds if stack else '0')
for (dv, av) in layout:
    Button(win, width = 5, height = 2, command = partial(cmd, av), border = 0, text = dv, font = ("Myriad", 21), fg = 'black' if dv != 'C' else 'white', bg = '#FEF3E2' if isinstance(av, int) or dv in '=.' else '#F08400' if dv != 'C' else '#F00600').grid(row = row + 1, column = col)
    row, col = (row + 1) if col == 3 else row, (col + 1) if col != 3 else 0
win.mainloop()