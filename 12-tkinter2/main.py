import tkinter
import random

canvas = tkinter.Canvas(width = 600, height = 500)
canvas.pack()

x = 3
xx = x
y = 10
d = 30

pocet = 598 // d    # // je celociselne delenie 7 // 3 = 2
for j in range(498 // d):
    for i in range(pocet):
        color = random.choice(("green", "red", "blue", "orange", "purple"))
        canvas.create_rectangle(x, y, x+d, y+d, fill = color)
        canvas.create_line(x, y, x+d, y+d)
        canvas.create_line(x, y+d, x+d, y)
        x = x + d  #nakresli stvorcek vedla dalsieho stvorceka
    y = y + d   #nakresli stvorcek pod stvorcekom
    x = xx

canvas.mainloop()