import turtle

def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

t = turtle.Turtle()
t.speed(2)

"""for j in range(4):
    for i in range(1, 11):
        stvorec(10 * i)
    t.left(90) """

"""t.fd(100)
t.penup()
t.fd(100)
t.pendown()
t.fd(100)"""

def stvorce(times):
    x = 23
    for i in range(1, times+1):
        stvorec(x)
        t.pu()
        t.right(135)
        t.fd(20)
        t.pd()
        t.left(135)
        x+= 30

stvorce(10)
turtle.mainloop()
