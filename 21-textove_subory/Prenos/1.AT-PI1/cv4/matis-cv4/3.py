# Slniecko Matis
import turtle
import tkinter
import random


t = turtle.Turtle()
turtle.delay(0)

pocet = 10
velkost = 100


def slnko(pocet, velkost):
    t.fillcolor("Gold")
    t.pencolor("Gold")
    t.begin_fill()
    for g in range(pocet):
        t.right(90)
        t.width(10)
        t.fd(velkost)
        t.fd(-velkost)
        t.left(90)
        t.fd(velkost / 360)
        t.left(360 / pocet)
    t.rt(90)
    t.fd(velkost / 2)
    t.rt(90)
    for i in range(360):
        t.fd(3.14 * velkost / 360)
        t.rt(1)
    t.end_fill()


def newSun():
    t.clear()
    pocet = random.randint(3, 20)
    velkost = random.randint(20, 100)
    slnko(pocet, velkost)



slnko(pocet, velkost)
turtle.mainloop()
