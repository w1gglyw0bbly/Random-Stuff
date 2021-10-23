import tkinter as tk
root = tk.Tk()

left = 'edwhrkieuwiiornnrthstooogthofhdrwiotsifss'
left = [string := x + '\n' for x in left]
left = ''.join(left)
right = 'hssthelaaenchamllnwoleniesdhtothndeeohsr'
right = [string := x + '\n' for x in right]
right = ''.join(right)


def leftSide():
    return 'cringe'
    
def rightSide():
    return 'cringe'

label1 = tk.Label(text = left)
label2 = tk.Label(text = right)
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1)

tk.mainloop()
