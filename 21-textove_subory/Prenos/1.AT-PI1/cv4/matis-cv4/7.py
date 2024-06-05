# Hviezda
import turtle

t = turtle.Turtle()
velkost = 100
farba1, farba2 = "tomato", "tan"


def kosostvorec(velkost):
    for i in range(2):
        t.fd(velkost)
        t.left(45)
        t.fd(velkost)
        t.left(135)


for j in range(8):
    t.fillcolor(farba1)
    t.begin_fill()
    kosostvorec(velkost)
    t.end_fill()
    t.left(360 / 8)
    farba1, farba2 = farba2, farba1
turtle.mainloop()
