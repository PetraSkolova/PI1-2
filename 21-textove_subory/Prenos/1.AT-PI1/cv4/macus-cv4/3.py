import turtle
import random
import tkinter

def slnko(pocet, velkost):
    t.pencolor('gold')
    t.pensize(10)
    for i in range(pocet):
        t.fd(velkost)
        t.fd(-velkost)
        t.rt(360 / pocet)
    t.dot(velkost)

def nove_slnko():
    t.clear()
    slnko(random.randint(3, 20), random.randint(20, 100))

turtle.delay(0)
t = turtle.Turtle()
tkinter.Button(text="Nové Slnko", command=nove_slnko).pack(side="left")
turtle.speed(100)
slnko(10,80)


turtle.done()