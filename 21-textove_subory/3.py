import tkinter

canvas = tkinter.Canvas()
canvas.pack()

fbody = open('body.txt', 'r')
for riadok in fbody:

    medzera = riadok.find(' ')
    tvar = riadok[ :medzera]
    riadok = riadok[medzera+1]

    medzera = riadok.find(' ')
    x = int(riadok[:medzera])
    riadok = riadok[medzera+1:]

    medzera = riadok.find(' ')
    y = int(riadok[medzera:])
    riadok = riadok[medzera+1:]

    medzera = riadok.find(' ')
    r = int(riadok[:medzera])
    riadok = riadok[medzera+1:]

    medzera = riadok.find(' ')
    g = int(riadok[:medzera])
    riadok = riadok[medzera+1:]

    medzera = riadok.find(' ')
    b = int(riadok[:medzera])
    riadok = riadok[medzera+1:]

    print(tvar, x, y)
    if tvar == 'r':
        canvas.create_rectangle(x, y, x + 20, y + 20)
    else:
        canvas.create_oval(x, y, x + 20, y + 20)

tkinter.mainloop()