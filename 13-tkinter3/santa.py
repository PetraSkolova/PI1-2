import tkinter
import time
import random

canvas_width = 500
canvas_height = 600
santa_x = canvas_width // 2
santa_y = 66
santa_posun = 1

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

image_santa = tkinter.PhotoImage(file="santa.png.png")
santa = canvas.create_image(canvas_width // 2, 66, image=image_santa)
while True:
    canvas.update()
    time.sleep(0.001)
    canvas.move(santa, 0, santa_posun)
    santa_y = santa_y + santa_posun     #y sa bude posuvat, pokial nedosiahne canvas_height + 64
    if santa_y == canvas_height + 64:
        canvas.delete(santa)
        santa_y = 66
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)
image_santa2 = tkinter.PhotoImage(file="santa.png.png")
santa2 = canvas.create_image(canvas_width, image=image_santa)

canvas.mainloop()
