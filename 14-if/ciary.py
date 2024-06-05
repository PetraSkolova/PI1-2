"""""
import tkinter
canvas_width = 300
canvas_height = canvas_width

polomer = 8
pocet = canvas_width // (polomer * 2)
x = polomer * 2
y = 0

canvas = tkinter.Canvas(bg="white", width=canvas_width, height=canvas_height)
canvas.pack()

for j in range(pocet):
    canvas.create_line(x , y, x, y+canvas_height)
    x = x + polomer * 2

tkinter.mainloop()
"""
import tkinter

width = 400
height = 400
d = 15  #polomer * 2, kruhy sa kreslia ako stvorce

x = 0
y1 = 0      # y1, aby sa lepsie orientovalo v ciarach

farba1, farba2 = "red", "blue"
canvas = tkinter.Canvas(width=width,height=height)
canvas.pack()

for i in range(width // d):
    canvas.create_line(x+d, 0, x+d, height, width=2, fill=farba1)
    farba1,farba2=farba2,farba1
    canvas.create_line(0,y1 + d, width, y1 + d, width=2, fill=farba2)
    x += d    # x = x + d
    y1 += d   # y = y + d
tkinter.mainloop()