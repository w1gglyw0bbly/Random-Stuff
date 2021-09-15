import tkinter as tk
import sys
from functools import partial
 
sys.path.append('.')
from MSTest import Minesweeper

def test(board, button, buttons, y, x):
    #print(buttonList)
    
    if countDisabled(buttons) == 0:
        print('hit')
        if board.fullBoard[y][x] != 0:
            while board.fullBoard[y][x] != 0:
                board.newFullBoard()
                if board.fullBoard[y][x] == 0:
                    break
    if board.fullBoard[y][x] == 'B':
        button.config(state = 'disabled', bg = 'red', text = str(board.fullBoard[y][x]))
    elif board.fullBoard[y][x] == 0:
        button.config(state = 'disabled', bg = 'light grey')
    elif board.fullBoard[y][x] == 1:
        button.config(state = 'disabled', bg = 'light green', text = str(board.fullBoard[y][x]))
    else:
        button.config(state = 'disabled', text = str(board.fullBoard[y][x]))

def countDisabled(buttons):
    numDisabled = 0
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            if buttons[i][j].cget('state') == 'disabled':
                numDisabled += 0
    return numDisabled



top = tk.Tk()
frame = tk.Frame(top)
frame.grid()

board = Minesweeper('Easy')

buttonList = []
for i in range(8):
    buttonRow = []
    for j in range(10):
        b = tk.Button(top, width = 5, height = 2)
        buttonRow.append(b)
        b.config(command = partial(test, board, b, buttonList, i, j))
        b.grid(row = i, column = j)
    buttonList.append(buttonRow)

 
top.mainloop()

