import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#
def button_func():
    print('a basic button')

button_string = tk.StringVar(value = 'A button with sting var')
button = ttk.Button(master = window, text = 'A simp button',command = button_func, textvariable = button_string)
button.pack()

#check button
check_var = tk.StringVar()
check = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command=lambda:print(check_var.get()),
    variable = check_var)
check.pack()

#run
window.mainloop()