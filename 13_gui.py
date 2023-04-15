import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Menu')
window.geometry('600x400')


#menu
menu = tk.Menu(window)

#sub menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'New', command= lambda: print('New file'))
file_menu.add_command(label = 'Open', command= lambda: print('Open file'))
file_menu.add_separator()

menu.add_cascade(label = 'File',menu = file_menu)

#another sub menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Help entry', command= lambda: print('help'))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='check',onvalue='on',offvalue='off',variable=help_check_string,command=lambda: print(help_check_string.get()))
menu.add_cascade(label = 'Help',menu = help_menu)

#ex menu
ex_menu = tk.Menu(menu, tearoff = False)
ex_menu.add_command(label = 'ex entry')
menu.add_cascade(label = 'Exercise',menu = ex_menu)

#ex sub menu
ex_sub_menu = tk.Menu(menu, tearoff = False)
ex_sub_menu.add_command(label = 'ex Sub menu')
ex_menu.add_cascade(label = 'more sstuff',menu = ex_sub_menu)

window.configure(menu = menu)

# menu button

menu_button = ttk.Menubutton(window, text = 'Menu button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button,tearoff = False)
button_sub_menu.add_command(label='entry 1', command = lambda: print('test 1'))
button_sub_menu.add_checkbutton(label='check 1')
#menu_button.configure(menu = button_sub_menu)
menu_button['menu']=button_sub_menu





window.mainloop()