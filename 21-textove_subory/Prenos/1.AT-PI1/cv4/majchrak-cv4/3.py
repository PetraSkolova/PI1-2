import turtle, tkinter, random


def tlacidlo():
    t.clear()
    slnko(random.randint(3, 20), random.randint(20, 100))


t = turtle.Turtle()
turtle.delay(0)
tkinter.Button(text="Nové slnko", command=tlacidlo).pack()


def slnko(pocet, velkost):
    t.pensize(10)
    t.pencolor("gold")
    for i in range(pocet):
        t.fd(velkost)
        t.rt(180)
        t.fd(velkost)
        t.rt(180)
        t.rt(360/pocet)
    t.dot(velkost, "gold")


slnko(15, 100)


turtle.mainloop()