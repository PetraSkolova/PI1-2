import tkinter as tk #as tk = odteraz staci pisat len skratku tk

root=tk.Tk()  #vytvori tk okno
canvas= tk.Canvas(root,width=800,height=600)
canvas.pack()

pivot=50

#pismeno P
canvas.create_arc(50,50,100,100,start=270,extent=180,style="arc",outline="blue",width=5)
canvas.create_line(75,50,75,200,fill="blue",width=5)
#pismeno E
canvas.create_line(200,50,120,50,120,100,120,200,200,200,120,200,fill="brown",width=2)
canvas.create_line(180,120,118,120,fill="brown",width=2)
#pismeno T
canvas.create_line(320,50,220,50,270,50,270,200,fill="purple",width=8)
#pismeno R
canvas.create_arc(310,50,400,100,start=270,extent=180,style="arc",outline="red",width=3)
canvas.create_line(355,100,355,200,fill="red",width=3)
canvas.create_line(355,100,400,200,fill="red",width=3)
canvas.create_line(355,50,355,100,fill="red",width=3)
#pismenon A
canvas.create_line(460,50,420,200,fill="green",width=6)
canvas.create_line(460,50,500,200,fill="green",width=6)
canvas.create_line(436,140,485,140,fill="green",width=6)
#pismeno Š
canvas.create_line(95,230,70,200,fill="black",width=4)
canvas.create_line(95,230,120,200,fill="black",width=4)
canvas.create_arc(55,230,150,300,start=10,extent=260,style="arc",outline="black",width=4)
canvas.create_arc(55,300,150,370,start=190,extent=260,style="arc",outline="black",width=4)
#pismeno K
canvas.create_line(170,230,170,370,fill="grey",width=2)
canvas.create_line(170,300,210,230,fill="grey",width=2)
canvas.create_line(170,300,210,370,fill="grey",width=2)
#pismeno O
canvas.create_oval(220,230,370,370,outline="orange",width=8)
#pismeno L
canvas.create_line(380,230,380,370,fill="light blue",width=7)
canvas.create_line(380,370,440,370,fill="light blue",width=7)
#pismeno O
canvas.create_oval(440,370,550,230,outline="magenta",width=12)
#pismeno V
canvas.create_line(560,230,600,370,fill="yellow",width=9)
canvas.create_line(630,230,600,370,fill="yellow",width=9)
#pismeno Á
canvas.create_line(640,370,690,230,fill="light green",width=11)
canvas.create_line(740,370,690,230,fill="light green",width=11)
canvas.create_line(660,320,723,320,fill="light green",width=11)
canvas.create_line(710,180,690,220,fill="light green",width=11)

canvas.mainloop()