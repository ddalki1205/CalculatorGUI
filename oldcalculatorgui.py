import tkinter as tk

win = tk.Tk()
win.title("Calculator")
win.geometry(f"{(width := int(win.winfo_screenwidth() / 2.85))}x{(height := int(win.winfo_screenheight() / 2.85))}+{(x := int((win.winfo_screenwidth() - width) / 2))}+{(y := int((win.winfo_screenheight() - height) / 2.2))}")
win.config(bg="#000000")
win.wm_attributes('-transparentcolor')

labels_info = [("Python GUI Basic Calculator v1", 160, 50, ("Century Gothic", 18)), ("First number", 20, 110, ("Century Gothic", 15)), ("Second number", 20, 150, ("Century Gothic", 15)), ("Result: ", 420, 110, ("Century Gothic", 15)), (" ", 420, 150, ("Century Gothic", 15))]
labels = []
for (text, x, y, (font, size)) in labels_info:
    label = tk.Label(win, text=text, font=(font, size), fg="white", bg="black")
    label.place(x=x, y=y)
    labels.append(label)

firstnum, secondnum = tk.Entry(win, font=("Century Gothic", 13), bg="black", fg="white"), tk.Entry(win, font=("Century Gothic", 13), bg="black", fg="white")
firstnum.place(x=200, y=110)
secondnum.place(x=200, y=150)
lblnresult = labels[4] 

def add():
    lblnresult.config(text=(int(firstnum.get()) + int(secondnum.get())), fg="green")
def minus():
    lblnresult.config(text=(int(firstnum.get()) - int(secondnum.get())), fg="green")
def mult():
    lblnresult.config(text=(int(firstnum.get()) * int(secondnum.get())), fg="green")
def div():
    lblnresult.config(text=(int(firstnum.get()) / int(secondnum.get())) if int(secondnum.get()) != 0 else "undefined", fg="green" if int(secondnum.get()) != 0 else "red")
def floor():
    lblnresult.config(text=(int(firstnum.get()) // int(secondnum.get())) if int(secondnum.get()) != 0 else "undefined", fg="green" if int(secondnum.get()) != 0 else "red")
def mod():
    lblnresult.config(text=(int(firstnum.get()) % int(secondnum.get())) if int(secondnum.get()) != 0 else "undefined", fg="green" if int(secondnum.get()) != 0 else "red")
def exp():
    lblnresult.config(text=(int(firstnum.get()) ** int(secondnum.get())), fg="green")

button_frame = tk.Frame(win, bg="black")
button_frame.place(x=50, y=245)

for (text, row, column, command) in [("+", 1, 0, add), ("-", 1, 1, minus), ("*", 1, 2, mult), ("/", 1, 3, div), ("//", 1, 4, floor), ("^", 1, 5, exp), ("%", 1, 6, mod)]:
    tk.Button(button_frame ,width=5, height=2, text=text, font=("Century Gothic", 15), fg="white", bg="black", command=command).grid(row=row,column=column, padx=6)

win.mainloop()