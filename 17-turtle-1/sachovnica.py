import turtle

t = turtle.Turtle()
t.speed(0)

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.left(90)

def sachovnica(dlzka, farba1, farba2):
    x = -200
    y = 200
    for i in range(8):
        for j in range(8):
            t.penup()
            t.setpos(x, y)
            t.pendown()
            t.fillcolor(farba1)
            t.begin_fill()
            stvorec(dlzka)
            t.end_fill()
            farba1, farba2 = farba2, farba1
            x += dlzka
        x -= (dlzka*8)
        y -= dlzka
        farba1, farba2 = farba2, farba1

sachovnica(20, "red", "blue")

turtle.mainloop()