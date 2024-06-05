import tkinter
import random

canvas = tkinter.Canvas(width = 600, height = 500)
canvas.pack()

x = 10
xx = x
y = 10
d = 40
stvrtina = d // 4

#canvas.create_rectangle(x,  y+d // 2, x+d, y+(d // 2)+d)
#canvas.create_polygon(x + d // 2, y, x+d, x+d, y+(d // 2)+d, x + d // 2, y)
pocet = 598 // d    # // je celociselne delenie 7 // 3 = 2
for j in range(498 // d):
    for i in range(pocet):
        canvas.create_rectangle(x,  y+d // 2, x+d, y+(d // 2)+d, fill="orange")
        canvas.create_polygon(x, y+d//2, x+2*stvrtina, y, x+d, y+d//2, outline="black", fill="red")
        canvas.create_rectangle(x+stvrtina, y+d // 2+stvrtina, x+3*stvrtina, y+d // 2+3*stvrtina, fill="light blue")
        #canvas.create_line(x+stvrtina, y+d // 2+2*stvrtina, x+3*stvrtina,y+d // 2+2*stvrtina)
        canvas.create_line(x+stvrtina, y+d // 2+2*stvrtina, x+3*stvrtina,y+d // 2+2*stvrtina)
        canvas.create_line(x+2*stvrtina, y+d // 2+stvrtina, x+2*stvrtina, y+d // 2+3*stvrtina)
        x = x + d
    y = y+float(3.55)*d//2
    x = xx

canvas.mainloop()
