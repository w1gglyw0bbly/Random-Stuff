import turtle as t
import tkinter as tk

root = tk.Tk()
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame1.grid(row = 0, column = 0, sticky = 'w')
frame2.grid(row = 0, column = 1, sticky = 'ne')

def tLeft():
    if t.heading() == 180.0:
        t.fd(50)
    else:
        t.lt(180 - int(t.heading()))
        t.fd(50)

def tRight():
    if t.heading() == 0.0:
        t.fd(50)
    elif t.heading() == 180.0:
        t.rt(180)
        t.fd(50)
    else:
        t.rt(180 - int(t.heading()))
        t.fd(50)

def tUp():
    if t.heading() == 90.0:
        t.fd(50)
    else:
        t.lt(90 - int(t.heading()))
        t.fd(50)
    
def tDown():
    if t.heading() == 270.0:
        t.fd(50)
    elif t.heading() == 90.0:
        t.rt(180)
        t.fd(50)
    else:
        t.rt(90 - int(t.heading()))
        t.fd(50)

def tColor():
    t.color('red')

def close():
    root.destroy()
    t.Screen().bye()
    
bLeft = tk.Button(frame1, text = 'Left', command = tLeft)
bRight = tk.Button(frame1, text = 'Right', command = tRight)
bUp = tk.Button(frame1, text = 'Up', command = tUp)
bDown = tk.Button(frame1, text = 'Down', command = tDown)
bExit = tk.Button(frame1, text = 'Exit', command = close)

colors = ('Red', 'Blue', 'Yellow', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Brown')
main = tk.StringVar(root, 'Colors')
current = tk.StringVar(frame2, 'Colors')

bColor = tk.OptionMenu(frame2, current, *colors, command = tColor)

for x in range(len(frame1.children)):
    print(len(frame1.children))
    frame1.winfo_children()[x].grid(row = x)

for x in range(len(frame2.children)):
    frame2.winfo_children()[x].grid(row = x)

tk.mainloop()
