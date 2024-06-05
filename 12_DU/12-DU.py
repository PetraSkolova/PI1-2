import tkinter as tk

x = 5
y = 5
d = 10
width = 630
height = 250

count = (width - x) // (29 * d)
count2 = (height - y) // (7 * d)

canvas = tk.Canvas(width=width, height=height)
canvas.pack()

print(count, count2)

for j in range(count2):
    for i in range(count):
        # pismeno P
        canvas.create_rectangle(x, y, x + d, y + d, fill="purple")
        canvas.create_rectangle(x, y + d, x + d, y + 2 * d, fill="purple")
        canvas.create_rectangle(x, y + 2 * d, x + d, y + 3 * d, fill="purple")
        canvas.create_rectangle(x, y + 3 * d, x + d, y + 4 * d, fill="purple")
        canvas.create_rectangle(x, y + 4 * d, x + d, y + 5 * d, fill="purple")
        canvas.create_rectangle(x, y + 5 * d, x + d, y + 6 * d, fill="purple")
        canvas.create_rectangle(x, y + 6 * d, x + d, y + 7 * d, fill="purple")

        canvas.create_rectangle(x + d, y, x + 2 * d, y + d, fill="purple")
        canvas.create_rectangle(x + 2 * d, y, x + 3 * d, y + d, fill="purple")
        canvas.create_rectangle(x + 3 * d, y, x + 4 * d, y + d, fill="purple")

        canvas.create_rectangle(x + 4 * d, y + d, x + 5 * d, y + 2 * d, fill="purple")
        canvas.create_rectangle(x + 4 * d, y + 2 * d, x + 5 * d, y + 3 * d, fill="purple")

        canvas.create_rectangle(x + d, y + 3 * d, x + 2 * d, y + 4 * d, fill="purple")
        canvas.create_rectangle(x + 2 * d, y + 3 * d, x + 3 * d, y + 4 * d, fill="purple")
        canvas.create_rectangle(x + 3 * d, y + 3 * d, x + 4 * d, y + 4 * d, fill="purple")
        # pismeno E
        canvas.create_rectangle(x + 6 * d, y, x + 7 * d, y + d, fill="light blue")
        canvas.create_rectangle(x + 6 * d, y + d, x + 7 * d, y + 2 * d, fill="light blue")
        canvas.create_rectangle(x + 6 * d, y + 2 * d, x + 7 * d, y + 3 * d, fill="light blue")
        canvas.create_rectangle(x + 6 * d, y + 3 * d, x + 7 * d, y + 4 * d, fill="light blue")
        canvas.create_rectangle(x + 6 * d, y + 4 * d, x + 7 * d, y + 5 * d, fill="light blue")
        canvas.create_rectangle(x + 6 * d, y + 5 * d, x + 7 * d, y + 6 * d, fill="light blue")
        canvas.create_rectangle(x + 6 * d, y + 6 * d, x + 7 * d, y + 7 * d, fill="light blue")

        canvas.create_rectangle(x + 7 * d, y + 3 * d, x + 8 * d, y + 4 * d, fill="light blue")
        canvas.create_rectangle(x + 8 * d, y + 3 * d, x + 9 * d, y + 4 * d, fill="light blue")
        canvas.create_rectangle(x + 9 * d, y + 3 * d, x + 10 * d, y + 4 * d, fill="light blue")

        canvas.create_rectangle(x + 7 * d, y, x + 8 * d, y + d, fill="light blue")
        canvas.create_rectangle(x + 8 * d, y, x + 9 * d, y + d, fill="light blue")
        canvas.create_rectangle(x + 9 * d, y, x + 10 * d, y + d, fill="light blue")
        canvas.create_rectangle(x + 10 * d, y, x + 11 * d, y + d, fill="light blue")

        canvas.create_rectangle(x + 7 * d, y + 6 * d, x + 8 * d, y + 7 * d, fill="light blue")
        canvas.create_rectangle(x + 8 * d, y + 6 * d, x + 9 * d, y + 7 * d, fill="light blue")
        canvas.create_rectangle(x + 9 * d, y + 6 * d, x + 10 * d, y + 7 * d, fill="light blue")
        canvas.create_rectangle(x + 10 * d, y + 6 * d, x + 11 * d, y + 7 * d, fill="light blue")
        # pismeno T
        canvas.create_rectangle(x + 12 * d, y, x + 13 * d, y + d, fill="yellow")
        canvas.create_rectangle(x + 13 * d, y, x + 14 * d, y + d, fill="yellow")
        canvas.create_rectangle(x + 14 * d, y, x + 15 * d, y + d, fill="yellow")
        canvas.create_rectangle(x + 15 * d, y, x + 16 * d, y + d, fill="yellow")
        canvas.create_rectangle(x + 16 * d, y, x + 17 * d, y + d, fill="yellow")

        canvas.create_rectangle(x + 14 * d, y + d, x + 15 * d, y + 2 * d, fill="yellow")
        canvas.create_rectangle(x + 14 * d, y + 2 * d, x + 15 * d, y + 3 * d, fill="yellow")
        canvas.create_rectangle(x + 14 * d, y + 3 * d, x + 15 * d, y + 4 * d, fill="yellow")
        canvas.create_rectangle(x + 14 * d, y + 4 * d, x + 15 * d, y + 5 * d, fill="yellow")
        canvas.create_rectangle(x + 14 * d, y + 5 * d, x + 15 * d, y + 6 * d, fill="yellow")
        canvas.create_rectangle(x + 14 * d, y + 6 * d, x + 15 * d, y + 7 * d, fill="yellow")
        # pismeno R
        canvas.create_rectangle(x + 18 * d, y, x + 19 * d, y + d, fill="pink")
        canvas.create_rectangle(x + 19 * d, y, x + 20 * d, y + d, fill="pink")
        canvas.create_rectangle(x + 20 * d, y, x + 21 * d, y + d, fill="pink")
        canvas.create_rectangle(x + 21 * d, y, x + 22 * d, y + d, fill="pink")

        canvas.create_rectangle(x + 18 * d, y + d, x + 19 * d, y + 2 * d, fill="pink")
        canvas.create_rectangle(x + 18 * d, y + 2 * d, x + 19 * d, y + 3 * d, fill="pink")
        canvas.create_rectangle(x + 18 * d, y + 3 * d, x + 19 * d, y + 4 * d, fill="pink")
        canvas.create_rectangle(x + 18 * d, y + 4 * d, x + 19 * d, y + 5 * d, fill="pink")
        canvas.create_rectangle(x + 18 * d, y + 5 * d, x + 19 * d, y + 6 * d, fill="pink")
        canvas.create_rectangle(x + 18 * d, y + 6 * d, x + 19 * d, y + 7 * d, fill="pink")

        canvas.create_rectangle(x + 22 * d, y + d, x + 23 * d, y + 2 * d, fill="pink")
        canvas.create_rectangle(x + 22 * d, y + 2 * d, x + 23 * d, y + 3 * d, fill="pink")

        canvas.create_rectangle(x + 19 * d, y + 3 * d, x + 20 * d, y + 4 * d, fill="pink")
        canvas.create_rectangle(x + 20 * d, y + 3 * d, x + 21 * d, y + 4 * d, fill="pink")
        canvas.create_rectangle(x + 21 * d, y + 3 * d, x + 22 * d, y + 4 * d, fill="pink")

        canvas.create_rectangle(x + 20 * d, y + 4 * d, x + 21 * d, y + 5 * d, fill="pink")
        canvas.create_rectangle(x + 21 * d, y + 5 * d, x + 22 * d, y + 6 * d, fill="pink")
        canvas.create_rectangle(x + 22 * d, y + 6 * d, x + 23 * d, y + 7 * d, fill="pink")
        # pismeno A
        canvas.create_rectangle(x + 24 * d, y + d, x + 25 * d, y + 2 * d, fill="orange")
        canvas.create_rectangle(x + 24 * d, y + 2 * d, x + 25 * d, y + 3 * d, fill="orange")
        canvas.create_rectangle(x + 24 * d, y + 3 * d, x + 25 * d, y + 4 * d, fill="orange")
        canvas.create_rectangle(x + 24 * d, y + 4 * d, x + 25 * d, y + 5 * d, fill="orange")
        canvas.create_rectangle(x + 24 * d, y + 5 * d, x + 25 * d, y + 6 * d, fill="orange")
        canvas.create_rectangle(x + 24 * d, y + 6 * d, x + 25 * d, y + 7 * d, fill="orange")

        canvas.create_rectangle(x + 25 * d, y, x + 26 * d, y + d, fill="orange")
        canvas.create_rectangle(x + 26 * d, y, x + 27 * d, y + d, fill="orange")
        canvas.create_rectangle(x + 27 * d, y, x + 28 * d, y + d, fill="orange")

        canvas.create_rectangle(x + 28 * d, y + d, x + 29 * d, y + 2 * d, fill="orange")
        canvas.create_rectangle(x + 28 * d, y + 2 * d, x + 29 * d, y + 3 * d, fill="orange")
        canvas.create_rectangle(x + 28 * d, y + 3 * d, x + 29 * d, y + 4 * d, fill="orange")
        canvas.create_rectangle(x + 28 * d, y + 4 * d, x + 29 * d, y + 5 * d, fill="orange")
        canvas.create_rectangle(x + 28 * d, y + 5 * d, x + 29 * d, y + 6 * d, fill="orange")
        canvas.create_rectangle(x + 28 * d, y + 6 * d, x + 29 * d, y + 7 * d, fill="orange")

        canvas.create_rectangle(x + 25 * d, y + 3 * d, x + 26 * d, y + 4 * d, fill="orange")
        canvas.create_rectangle(x + 26 * d, y + 3 * d, x + 27 * d, y + 4 * d, fill="orange")
        canvas.create_rectangle(x + 27 * d, y + 3 * d, x + 28 * d, y + 4 * d, fill="orange")
        x = x + 30 * d
    x = x - 30 * d * count
    y = y + 8 * d
canvas.mainloop()