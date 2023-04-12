import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('Silder')
window.geometry('600x400')

#slider
scale_int = tk.IntVar(value = 15)
scale = ttk.Scale(
    window,
    command = lambda value: print(scale_int.get()),
    from_ = 0 ,
    to = 25,
    length = 300,
    orient = 'horizontal',
    variable = scale_int)
scale.pack()

#progress var
progress = ttk.Progressbar(
    window, 
    variable = scale_int, 
    maximum = 25,
    orient='horizontal',
    mode = 'determinate',
    length = 100)
progress.pack()

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 10)
scrolled_text.pack()

# exercise
scale_int1 = tk.IntVar()

progress1 = ttk.Progressbar(
    window, 
    variable = scale_int1, 
    orient='vertical',
    mode = 'determinate')
progress1.pack()
progress1.start()

label = ttk.Label(window,textvariable=scale_int1)
label.pack()

scale = ttk.Scale(
    window,
    from_ = 0 ,
    to = 100,
    variable = scale_int1)
scale.pack()

window.mainloop()