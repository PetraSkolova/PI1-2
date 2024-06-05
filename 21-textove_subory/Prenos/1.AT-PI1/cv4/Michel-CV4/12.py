import turtle

t = turtle.Turtle()
t.speed(0)

def stvorce(dlzka, krok):

    t.penup()
    t.begin_fill()
    t.fillcolor('red')
    for i in range(4):
        t.forward(dlzka)
        t.left(90)
    t.pendown()
    t.end_fill()

    t.penup()
    t.forward(krok)
    t.left(90)
    t.forward(krok)
    t.right(90)

    t.penup()
    t.begin_fill()
    t.fillcolor('blue')
    for i in range(4):
        t.forward(dlzka-2*krok)
        t.left(90)
    t.pendown()
    t.end_fill()


stvorce(100,10)

turtle.mainloop()