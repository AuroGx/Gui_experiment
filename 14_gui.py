import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('More on window')
#window.geometry('600x400')

# the icon you see in the file menu
#window.iconbitmap('image_file_name.ico')

#exercise centralize the app
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width /2)
top = int(display_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

#window sizes
window.minsize(200,100)
#window.maxsize(800,700)
#window.resizable(True,False)

#screen attributes of you own computer screen
print(window.winfo_screenwidth())
print(window.winfo_screenheight())




#window attributes
window.attributes('-alpha',1)


# security event
window.bind('<Escape>', lambda event: window.quit())

#title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0 , rely=1.0,anchor='se')


window.mainloop()