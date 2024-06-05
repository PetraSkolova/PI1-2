import tkinter

#canvas_width = 300
#canvas_height = 300

#canvas = tkinter.Canvas()
#canvas.pack()

#for i in range(pocet):
#    for j in range(pocet):
#       x = j*20 + 10
#        y = i*20 + 15
#        if i == 5:
#            farba = 'red'
#        else:
#            farba = 'white'
#        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=farba)

#tkinter.mainloop()

canvas_width = 600
canvas_height = canvas_width
polomer = 20
pocet = canvas_width // (polomer * 2)

canvas = tkinter.Canvas(bg="white", width=canvas_width, height=canvas_width)
canvas.pack()

for i in range(pocet):   #riadky
   for j in range(pocet):  #stlpce
       x = j * polomer * 2 + polomer
       y = i * polomer * 2 + polomer
       if j == pocet // 2:              #j == i or j == pocet - i - 1: nakresli krizik
           farba = "red"
       else:
           farba = "white"
       canvas.create_oval(x - polomer, y - polomer, x + polomer, y + polomer, fill=farba)
tkinter.mainloop()