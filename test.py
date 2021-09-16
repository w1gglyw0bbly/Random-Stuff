import tkinter as tk
import sys
from functools import partial
 
sys.path.append('.')
from MSTest import Minesweeper

def test(board, button, buttons, y, x):
    #print(buttonList)
    
    if countDisabled(buttons) == 0:
        #print('hit')
        if board.fullBoard[y][x] != 0:
            while board.fullBoard[y][x] != 0:
                board.newFullBoard()
                if board.fullBoard[y][x] == 0:
                    break
    output = buttonClicked(button, y, x)
    if output == '0':
        checkSurrounding(buttons, y, x, button)

def buttonClicked(button, y, x):
    if board.fullBoard[y][x] == 'B':
        button.config(state = 'disabled', bg = 'red', text = str(board.fullBoard[y][x]))
    elif board.fullBoard[y][x] == 0:
        button.config(state = 'disabled', bg = 'light grey')
    elif board.fullBoard[y][x] == 1:
        button.config(state = 'disabled', bg = 'light green', text = str(board.fullBoard[y][x]))
    elif board.fullBoard[y][x] == 2:
        button.config(state = 'disabled', bg = 'pink', text = str(board.fullBoard[y][x]))
    elif board.fullBoard[y][x] == 3:
        button.config(state = 'disabled', bg = 'light blue', text = str(board.fullBoard[y][x]))
    elif board.fullBoard[y][x] == 4:
        button.config(state = 'disabled', bg = 'purple', text = str(board.fullBoard[y][x]))     
    else:
        button.config(state = 'disabled', text = str(board.fullBoard[y][x]))
    return str(board.fullBoard[y][x])

def countDisabled(buttons):
    numDisabled = 0
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            if buttons[i][j].cget('state') == 'disabled':
                numDisabled += 1
    return numDisabled

def checkSurrounding(buttons, y, x, b):
    dump = 0
    
    #UL
    if y - 1 < 0 or x - 1 < 0:
        dump += 1
    else:
        buttonClicked(buttons[y - 1][9 + (x - 9) - 1], y - 1, 9 + (x - 9) - 1)
    #U
    if y - 1 < 0:
        dump += 1
    else:
        buttonClicked(buttons[y - 1][9 + (x - 9)], y - 1, 9 + (x - 9))
    #UR
    if y - 1 < 0 or x + 1 > board.getRowEnd() - 1:
        dump += 1
    else:
        print('hit UR')
        buttonClicked(buttons[y - 1][9 + (x - 9) + 1], y - 1, 9 + (x - 9) + 1)
    #R
    if x + 1 > board.getRowEnd() - 1:
        dump += 1
    else:
        print('hit R')
        buttonClicked(buttons[y][x + 1], y, x + 1)
    #BR
    if y + 1 > 7 or x + 1 > board.getRowEnd() - 1:
        dump += 1
    else:
        print('hit BR')
        buttonClicked(buttons[y + 1][9 - (9 - x) + 1], y + 1, 9 - (9 - x) + 1)
    #B
    if y + 1 > 7:
        dump += 1
    else:
        print('hit B')
        buttonClicked(buttons[y + 1][9 - (9 - x)], y + 1, 9 - (9 - x))
    #BL
    if y + 1 > 7 or x - 1 < 0:
        dump += 1
    else:
        print('hit BL')
        buttonClicked(buttons[y + 1][9 - (9 - x) - 1], y + 1, 9 - (9 - x) - 1)
    #L
    if x - 1 < 0:
        dump += 1
    else:
        print('hit L')
        buttonClicked(buttons[y][x - 1], y, x - 1)
        
        
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

