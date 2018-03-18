from tkinter import *

w = Canvas(Tk(), width=900, height=400)
w.pack()

for i in range(300):
    x = i * 3
    if i % 2 == 0:
        c = "#FF0000"
    else:
        c = "#0000FF"
    w.create_line(x, 0, x, 400, fill=c)

mainloop()
