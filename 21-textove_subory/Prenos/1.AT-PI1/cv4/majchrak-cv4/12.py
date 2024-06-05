import turtle, random


def stvorce(dlzka, krok):
    t.penup()
    t.fd(dlzka/2)
    t.rt(90)
    t.fd(dlzka/2)
    t.rt(90)
    while dlzka>0:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"#{r:02x}{g:02x}{b:02x}"
        t.fillcolor(color)
        t.begin_fill()
        for i in range(4):
            t.fd(dlzka)
            t.rt(90)
        dlzka -= krok
        t.end_fill()
        t.fd(krok/2)
        t.rt(90)
        t.fd(krok/2)
        t.rt(270)


t = turtle.Turtle()
turtle.delay(0)


stvorce(200, 25)
turtle.mainloop()