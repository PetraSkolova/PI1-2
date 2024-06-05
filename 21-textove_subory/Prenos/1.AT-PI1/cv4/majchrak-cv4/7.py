import turtle


def kosostvorec(velkost, farba1, farba2):
    for i in range(8):
        t.fillcolor(farba1)
        t.begin_fill()
        for j in range(2):
            t.fd(velkost)
            t.left(45)
            t.fd(velkost)
            t.left(135)
        t.end_fill()
        farba1, farba2 = farba2, farba1
        t.left(45)


t = turtle.Turtle()
turtle.delay(0)


kosostvorec(100, "tomato", "tan")


turtle.mainloop()