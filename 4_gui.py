import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

#window
window = tk.Tk()
window.title('tkinter variable')


#tkinter variable
string_var = tk.StringVar()

#widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

# exercise

#tkinter variable
string_var1 = tk.StringVar( value = 'test')

entry1 = ttk.Entry(master = window, textvariable = string_var1)
entry1.pack()

entry2 = ttk.Entry(master = window, textvariable = string_var1)
entry2.pack()

label1 = ttk.Label(master = window, text = 'label', textvariable = string_var1)
label1.pack()

#run
window.mainloop()