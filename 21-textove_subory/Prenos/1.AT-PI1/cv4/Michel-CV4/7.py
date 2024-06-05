import turtle

t = turtle.Turtle()
t.speed(0)

def kosostvorec(velkost, farba):
    t.begin_fill()
    if farba == 1:
        t.fillcolor('tomato')
    else:
        t.fillcolor('tan')
    for i in range(2):
        t.forward(velkost)
        t.left(45)
        t.forward(velkost)
        t.left(135)
    t.end_fill()
def kosostvorce(velkost):
    for i in range(4):
        kosostvorec(velkost,1)
        t.left(45)
        kosostvorec(velkost, 2)
        t.left(45)

kosostvorce(100)

turtle.mainloop()