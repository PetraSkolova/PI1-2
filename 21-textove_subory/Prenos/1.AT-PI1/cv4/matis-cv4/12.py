import turtle
import random

# stvorce
t = turtle.Turtle()
turtle.delay(0)
velkost = 200
krok = 25


def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def stvorec(velkost):
    for i in range(4):
        t.fd(velkost)
        t.left(90)


def stvorce(velkost, krok):
    t.pencolor("")
    for i in range(velkost // krok):
        t.fillcolor(rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        t.begin_fill()
        stvorec(velkost)
        t.end_fill()
        t.left(90)
        t.fd(krok / 2)
        t.right(90)
        t.fd(krok / 2)
        velkost -= krok


stvorce(velkost, krok)

turtle.mainloop()
