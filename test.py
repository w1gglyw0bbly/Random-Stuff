import tkinter as tk
import sys
from functools import partial

sys.path.append('.')
from MSTest import Minesweeper

def test(board, button, y, x):
    if board.fullBoard[y][x] == 'B':
        button.config(state = 'disabled', bg = 'red', text = str(board.fullBoard[y][x]))
    elif board.fullBoard[y][x] == 0:
        button.config(state = 'disabled', bg = 'light grey')
    elif board.fullBoard[y][x] == 1:
        button.config(state = 'disabled', bg = 'light green', text = str(board.fullBoard[y][x]))
    else:
        button.config(state = 'disabled', text = str(board.fullBoard[y][x]))


top = tk.Tk()
frame = tk.Frame(top)
frame.grid()

board = Minesweeper('Easy')

for i in range(8):
    for j in range(10):
        if board.fullBoard[i][j] == 'B':
            b = tk.Button(top, width = 5, height = 2)
            b.config(command = partial(test, board, b, i, j))
        else:
            b = tk.Button(top, width = 5, height = 2)
            b.config(command = partial(test, board, b, i, j))

        b.grid(row = i, column = j)


top.mainloop()
