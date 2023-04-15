import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Tabs')
window.geometry('600x400')


#notebooks widget
notebook = ttk.Notebook(window)

#tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = "Text in Tab1")
label1.pack()
button1 = ttk.Button(tab1, text = 'Button in tab1')
button1.pack()


#tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = "Text in Tab2")
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()


notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')

tab3 = ttk.Frame(notebook)
label3 = ttk.Label(tab3, text = "Text in Tab3")
label3.pack()
button3 = ttk.Button(tab3, text = 'Button in tab3')
button3.pack()  

notebook.add(tab3, text = 'Tab 3')

notebook.pack()



window.mainloop()