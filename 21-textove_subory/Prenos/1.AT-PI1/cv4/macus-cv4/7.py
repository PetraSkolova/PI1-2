import turtle

def kosostvorec(velkost, farba):
    t.fillcolor(farba)
    t.begin_fill()
    for j in range(8):
        t.fd(velkost)
        t.rt(45)
        t.fd(velkost)
        t.rt(135)
    t.end_fill()

turtle.delay(0)
t = turtle.Turtle()
for i in range(8):
    kosostvorec(100, ('tan', 'tomato')[i % 2])
    t.lt(45)

turtle.done()