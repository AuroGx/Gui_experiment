import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Frames and parenting')
window.geometry('600x400')


#frames
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
#This line makes it that the border of the frame doesnt shrink to the size of the widgets in it, Default = True
frame.pack_propagate(False)
frame.pack(side ='left')


#parenting
label = ttk.Label(frame, text= 'Label in frame')
label.pack()

button = ttk.Button(frame,text = 'Button in a Frame')
button.pack()


label2 = ttk.Label(window, text= 'Label out of frame')
label2.pack()

#exercise
frame2 = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
#This line makes it that the border of the frame doesnt shrink to the size of the widgets in it, Default = True
frame2.pack_propagate(False)
frame2.pack(side ='right')

label3 = ttk.Label(frame2, text= 'Label in frame')
label3.pack()

button2 = ttk.Button(frame2,text = 'Button in a Frame')
button2.pack()

entry = ttk.Entry(frame2,text = 'Button in a Frame')
entry.pack()



window.mainloop()