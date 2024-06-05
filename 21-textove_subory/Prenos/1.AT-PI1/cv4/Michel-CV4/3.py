import turtle

t = turtle.Turtle()
t.speed(0)
#def slnko(pocet,velkost):
vekost = 3
t.pencolor('gold')
t.begin_fill()
t.fillcolor('gold')
for i in range(360):
    t.forward(10)
    t.right(1)
t.end_fill()

t.setpos(100,0)

turtle.mainloop()