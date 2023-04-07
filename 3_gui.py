import tkinter as tk
from tkinter import ttk

def button_func():
    #get the content of the entry
    entry_text = entry.get()

    #update the label
    #label.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'


#window
window = tk.Tk()
window.title('Getting and setting widgets')

#widgets
label = ttk.Label(master=window,text = 'A label')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text = 'a button', command = button_func)
button.pack()

def button1_func():
    #changes the text back to some text and enables entry, a reset button
    label['text'] = 'some text'
    entry['state'] = 'enabled'
  

#exercise
button2 = ttk.Button(master=window, text = '2nd button', command = button1_func)
button2.pack()

#run
window.mainloop()