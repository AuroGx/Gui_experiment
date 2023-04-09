import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value = 'A button with sting var')
button = ttk.Button(master = window, text = 'A simp button',command = button_func, textvariable = button_string)
button.pack()

#check button
check_var = tk.IntVar( value = 10)
check = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command=lambda:print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'Checkbox 2',
    command = lambda: print('test')
)
check2.pack()

#  radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'Radiobutton 1',
    value = 'radio 1',
    variable = radio_var,
    command= lambda : print(radio_var.get()))
radio1.pack()


radio2 = ttk.Radiobutton(
    window,
    text = 'Radiobutton 2',
    variable = radio_var,
    value = 2)
radio2.pack()

#exercise
def radio_func():
    print(check_var3.get())
    check_var3.set(False)


check_var3 = tk.BooleanVar()
radio_var3 = tk.StringVar()

check3 = ttk.Checkbutton(
    window,
    text = 'checkbox 3',
    command=lambda:print(radio_var3.get()),
    variable = check_var3)
check3.pack()




radio3 = ttk.Radiobutton(
    window,
    text = 'Radiobutton A',
    value = 'A',
    variable = radio_var3,
    command= radio_func)
radio3.pack()


radio4 = ttk.Radiobutton(
    window,
    text = 'Radiobutton B',
    variable = radio_var3,
    value = 'B',
    command= radio_func)
radio4.pack()


#run
window.mainloop()