import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')

def button1_func():
    print('Hello')

# window
window = tk.Tk()
#title
window.title('Window and Widgets')
# w x h of app screen
window.geometry('800x500')

#create widgets

#ttk label
label = ttk.Label(master = window, text = 'this is a test')
label.pack() 

# creates a text box. places it under the main window. and pack displays it
#tk.text
text = tk.Text(master = window)
text.pack()

#ttk entry, one liner text box
entry = ttk.Entry(master=window)
entry.pack()

#myttk label
label1 = ttk.Label(master = window, text = 'my label')
label1.pack() 

#my button
#button1 = ttk.Button(master=window, text = 'hello Button', command = button1_func )
button1 = ttk.Button(master=window, text = 'hello Button', command = lambda:print('gello') )
button1.pack()


#ttk button
button = ttk.Button(master=window, text = 'A Button', command = button_func )
button.pack()



# run
window.mainloop()