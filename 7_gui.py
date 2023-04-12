import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Combo and Spin')
window.geometry('600x500')

items = ['Ice Cream','Pizza','Broccoli']
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable= food_string)
combo['values'] = items
# combo.configure(values = items)
combo.pack()

#events
combo.bind('<<ComboboxSelected>>',lambda event: combo_label.config(text = f'selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

#spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(window, from_=3, to=20,increment=3,command=lambda: print(spin_int.get()), textvariable=spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('Down'))
spin.pack()

#exercise:

exercise_letters = ['A','B','C','D','E']
exercise_string = tk.StringVar(value=exercise_letters[0])
exercise_spin=ttk.Spinbox(window, textvariable = exercise_string,values = exercise_letters)
exercise_spin.pack()

exercise_spin.bind('<<Decrement>>',lambda event: print(exercise_string.get()))

window.mainloop()