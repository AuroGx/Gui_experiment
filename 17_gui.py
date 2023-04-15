import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Pack')
window.geometry('600x400')

# Top frame
top_frame = ttk.Frame(window)
label1= ttk.Label(top_frame,text ='First Label',background='red')
label2= ttk.Label(top_frame,text ='Label 2',background='blue')

#middle widget
label3= ttk.Label(window,text ='Another Label',background='green')

#bottom fram
bottom_frame =ttk.Frame(window)
label4= ttk.Label(bottom_frame ,text ='last Label',background='orange')
button1 = ttk.Button(bottom_frame ,text='button 1')
button2 = ttk.Button(bottom_frame ,text='button 2')


#top layout
label1.pack(fill='both',expand = True)
label2.pack(fill='both',expand = True)
top_frame.pack(fill='both',expand = True)

#middle layout
label3.pack(expand = True)


#bottom layout
button1.pack(side = 'left', expand = True , fill = 'both')
label4.pack(side = 'left', expand = True , fill = 'both')
button2.pack(side = 'left', expand = True , fill = 'both')
bottom_frame.pack(expand=True, fill = 'both',padx=20,pady=20)

# exercise
exercise_frame = ttk.Frame(bottom_frame)
button11 = ttk.Button(exercise_frame ,text='button 4')
button12 = ttk.Button(exercise_frame ,text='button 5')
button13 = ttk.Button(exercise_frame ,text='button 6')

button11.pack(side = 'top', expand = True , fill = 'both')
button12.pack(side = 'top', expand = True , fill = 'both')
button13.pack(side = 'top', expand = True , fill = 'both')
exercise_frame.pack(side = 'left', expand = True , fill = 'both',padx=10,pady=10)

window.mainloop()