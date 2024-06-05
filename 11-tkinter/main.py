import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 100
y = 50
dlzka = 20
canvas.create_rectangle(x, y, x + dlzka, y + dlzka, fill="red")
canvas.create_rectangle(x + dlzka, y, x + (2*dlzka), y + dlzka, fill="blue")
canvas.create_rectangle(x + (2*dlzka), y, x + (3*dlzka), y + dlzka, fill="red")
canvas.create_oval(x + dlzka, y + dlzka, x + (2*dlzka), y + (2*dlzka), fill="blue")
canvas.create_oval(x + dlzka, y + (2*dlzka), x + (2*dlzka), y + (3*dlzka), fill="blue")
canvas.create_rectangle(x + dlzka, y + (3*dlzka), x + (2*dlzka), y + (4*dlzka), fill="blue")
canvas.create_rectangle(x, y + (3*dlzka), x + dlzka, y + (4*dlzka), fill="red")
canvas.create_rectangle(x + (2*dlzka), y + (3*dlzka), x + (3*dlzka), y + (4*dlzka), fill="red")
canvas.mainloop()