import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Cavnas')
window.geometry('600x400')

# canvas
canvas = tk.Canvas(window,bg = 'white')
canvas.pack()

#canvas.create_rectangle((left,top,right,bottom))
canvas.create_rectangle((50,20,100,200),fill='red',width=10)
canvas.create_oval((200,0,300,100),fill = 'green')
canvas.create_arc((200,0,300,100),fill = 'red',start = 45,extent = 140,style = tk.CHORD, outline = 'red',width = 1)

#canvas.create_line((start_x,start_y,end_x,end_y))
canvas.create_line((0,0,100,150),fill = 'blue')

#canvas.create_polygon((x1,y1,x2,y2,x3,y3))
canvas.create_polygon((0,0,100,200,300,50,150,-50),fill = 'gray')


def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2),fill='black')


def brush_size_adjustment(event):
    global brush_size
    if event.delta > 0:
        brush_size +=4
    elif event.delta < 0:
        brush_size -=4


    brush_size = max(0,min(brush_size,50))


brush_size = 4
canvas.bind('<Motion>',draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjustment) 



window.mainloop()