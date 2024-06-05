import turtle
import random

def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

t = turtle.Turtle()
t.speed(0)

pocet = 50

for i in range(pocet):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.setheading(random.randint(0, 359))
    t.penup()           # t.setpos(random.randint(-200, 200), random.randint(-200, 200))
    t.setpos(x, y)
    t.pendown()
    stvorec(30)
    t.fillcolor(random.choice(("red", "green", "blue", "yellow")))
    t.begin_fill()
    stvorec(30)
    t.end_fill()

turtle.mainloop()