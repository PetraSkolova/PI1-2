import tkinter

canvas = tkinter.Canvas(width=300, height=100)
canvas.pack()
x = 5
y = 5
d = 10

# pismeno P
canvas.create_rectangle(x, y, x+d, y+d)
canvas.create_rectangle(x, y+d, x+d, y+2*d)
canvas.create_rectangle(x, y+2*d, x+d, y+3*d)
canvas.create_rectangle(x, y+3*d, x+d, y+4*d)
canvas.create_rectangle(x, y+4*d, x+d, y+5*d)
canvas.create_rectangle(x, y+5*d, x+d, y+6*d)
canvas.create_rectangle(x, y+6*d, x+d, y+7*d)

canvas.create_rectangle(x+d, y, x+2*d, y+d)
canvas.create_rectangle(x+2*d, y, x+3*d, y+d)
canvas.create_rectangle(x+3*d, y, x+4*d, y+d)

canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d)
canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d)

canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d)
canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d)
# pismeno E
canvas.create_rectangle(x+6*d, y, x+7*d, y+d)
canvas.create_rectangle(x+6*d, y+d, x+7*d, y+2*d)
canvas.create_rectangle(x+6*d, y+2*d, x+7*d, y+3*d)
canvas.create_rectangle(x+6*d, y+3*d, x+7*d, y+4*d)
canvas.create_rectangle(x+6*d, y+4*d, x+7*d, y+5*d)
canvas.create_rectangle(x+6*d, y+5*d, x+7*d, y+6*d)
canvas.create_rectangle(x+6*d, y+6*d, x+7*d, y+7*d)

canvas.create_rectangle(x+7*d, y+3*d, x+8*d, y+4*d)
canvas.create_rectangle(x+8*d, y+3*d, x+9*d, y+4*d)
canvas.create_rectangle(x+9*d, y+3*d, x+10*d, y+4*d)

canvas.create_rectangle(x+7*d,y, x+8*d, y+d)
canvas.create_rectangle(x+8*d, y, x+9*d, y+d)
canvas.create_rectangle(x+9*d, y, x+10*d, y+d)
canvas.create_rectangle(x+10*d, y, x+11*d, y+d)

canvas.create_rectangle(x+7*d, y+6*d, x+8*d, y+7*d)
canvas.create_rectangle(x+8*d, y+6*d, x+9*d, y+7*d)
canvas.create_rectangle(x+9*d, y+6*d, x+10*d, y+7*d)
canvas.create_rectangle(x+10*d, y+6*d, x+11*d, y+7*d)
# pismeno T
canvas.create_rectangle(x+12*d, y, x+13*d, y+d)
canvas.create_rectangle(x+13*d, y, x+14*d, y+d)
canvas.create_rectangle(x+14*d, y, x+15*d, y+d)
canvas.create_rectangle(x+15*d, y, x+16*d, y+d)
canvas.create_rectangle(x+16*d, y, x+17*d, y+d)

canvas.create_rectangle(x+14*d, y+d, x+15*d, y+2*d)
canvas.create_rectangle(x+14*d, y+2*d, x+15*d, y+3*d)
canvas.create_rectangle(x+14*d, y+3*d, x+15*d, y+4*d)
canvas.create_rectangle(x+14*d, y+4*d, x+15*d, y+5*d)
canvas.create_rectangle(x+14*d, y+5*d, x+15*d, y+6*d)
canvas.create_rectangle(x+14*d, y+6*d, x+15*d, y+7*d)
# pismeno R
canvas.create_rectangle(x+18*d, y, x+19*d, y+d)
canvas.create_rectangle(x+19*d, y, x+20*d, y+d)
canvas.create_rectangle(x+20*d, y, x+21*d, y+d)
canvas.create_rectangle(x+21*d, y, x+22*d, y+d)

canvas.create_rectangle(x+18*d, y+d, x+19*d, y+2*d)
canvas.create_rectangle(x+18*d, y+2*d, x+19*d, y+3*d)
canvas.create_rectangle(x+18*d, y+3*d, x+19*d, y+4*d)
canvas.create_rectangle(x+18*d, y+4*d, x+19*d, y+5*d)
canvas.create_rectangle(x+18*d, y+5*d, x+19*d, y+6*d)
canvas.create_rectangle(x+18*d, y+6*d, x+19*d, y+7*d)

canvas.create_rectangle(x+22*d, y+d, x+23*d, y+2*d)
canvas.create_rectangle(x+22*d, y+2*d, x+23*d, y+3*d)

canvas.create_rectangle(x+19*d, y+3*d, x+20*d, y+4*d)
canvas.create_rectangle(x+20*d, y+3*d, x+21*d, y+4*d)
canvas.create_rectangle(x+21*d, y+3*d, x+22*d, y+4*d)

canvas.create_rectangle(x+20*d, y+4*d, x+21*d, y+5*d)
canvas.create_rectangle(x+21*d, y+5*d, x+22*d, y+6*d)
canvas.create_rectangle(x+22*d, y+6*d, x+23*d, y+7*d)
# pismeno A
canvas.create_rectangle(x+24*d, y+d, x+25*d, y+2*d)
canvas.create_rectangle(x+24*d, y+2*d, x+25*d, y+3*d)
canvas.create_rectangle(x+24*d, y+3*d, x+25*d, y+4*d)
canvas.create_rectangle(x+24*d, y+4*d, x+25*d, y+5*d)
canvas.create_rectangle(x+24*d, y+5*d, x+25*d, y+6*d)
canvas.create_rectangle(x+24*d, y+6*d, x+25*d, y+7*d)

canvas.create_rectangle(x+25*d, y, x+26*d, y+d)
canvas.create_rectangle(x+26*d, y, x+27*d, y+d)
canvas.create_rectangle(x+27*d, y, x+28*d, y+d)

canvas.create_rectangle(x+28*d, y+d, x+29*d, y+2*d)
canvas.create_rectangle(x+28*d, y+2*d, x+29*d, y+3*d)
canvas.create_rectangle(x+28*d, y+3*d, x+29*d, y+4*d)
canvas.create_rectangle(x+28*d, y+4*d, x+29*d, y+5*d)
canvas.create_rectangle(x+28*d, y+5*d, x+29*d, y+6*d)
canvas.create_rectangle(x+28*d, y+6*d, x+29*d, y+7*d)

canvas.create_rectangle(x+25*d, y+3*d, x+26*d, y+4*d)
canvas.create_rectangle(x+26*d, y+3*d, x+27*d, y+4*d)
canvas.create_rectangle(x+27*d, y+3*d, x+28*d, y+4*d)

canvas.mainloop()