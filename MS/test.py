import tkinter as tk
from tkinter.ttk import *
import sys
from functools import partial
import tkinter.messagebox
from tkinter import *

#sys.path.append('.')
from MSTest import Minesweeper




def click(board, button, buttons, y, x):
    #print(buttonList)

    #checkWinCond(board, buttons)
    
    #Ensures that you start the game on a blank space so you cannot fail immediately
    if countDisabled(buttons) == 0:
        #print('hit')
        if board.fullBoard[y][x] != 0:
            while board.fullBoard[y][x] != 0:
                board.newFullBoard()
                if board.fullBoard[y][x] == 0:
                    break


    '''
    #counts number of bombs
    numBombs = 0
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            if buttons[i][j].cget('text') == 'B' or board.fullBoard[i][j] == 'B':
                numBombs += 1

    #print(numBombs)
    '''

    output = buttonClicked(board, button, y, x)
    #Reveals board if bomb is revealed, should change to just reveal all bombs
    endGame(board, output, buttons)

    #Reveals the surrounding of blank space and adjacents when revealed
    if output == '0':
        checkSurrounding(board, buttons, y, x, board.getRowEnd(), board.getColEnd())

    top.after(10, checkWinCond(board, buttons))




def buttonClicked(board, button, y, x):
    if board.fullBoard[y][x] == 'B':
        button.config(state = 'disabled', bg = 'red', text = str(board.fullBoard[y][x]))
    elif board.fullBoard[y][x] == 0:
        button.config(state = 'disabled', bg = 'light grey', text = '')
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

def checkWinCond(board, buttons):
    countChecked = 0
    #print('hit')
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            if buttons[i][j].cget('state') == 'disabled':
                countChecked += 1
    #print(countChecked)
    
    if (board.getRowEnd() + 1) * (board.getColEnd() + 1) - len(board.getBombs()) == countChecked:
        #print('hit good')
        endGame(board, 'B', buttons)
        tk.messagebox.showinfo('Nice', 'Nice')
    
    '''#print('hit flags')
    count = 0
    for i in range(board.getColEnd() + 1):
        for j in range(board.getRowEnd() + 1):
            #print(str(buttons[i][j].cget('text')) + ' ' + str(board.fullBoard[i][j]))
            if buttons[i][j].cget('text') == 'F' and board.fullBoard[i][j] == 'B':
                count += 1
    #print(count)
    if count == board.getDiffBombNum():
        #print('hit')
        endGame(board, 'B', buttons)
        tk.messagebox.showinfo('Nice', 'Nice')'''

def endGame(board, output, buttons):
    #Reveals board if bomb is revealed, should change to just reveal all bombs
    if output == 'B':
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                if buttons[i][j].cget('state') == 'disabled':
                    continue
                else:
                    buttonClicked(board, buttons[i][j], i, j)

def countDisabled(buttons):
    numDisabled = 0
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            if buttons[i][j].cget('state') == 'disabled':
                numDisabled += 1
    return numDisabled

def checkSurrounding(board, buttons, y, x, rowEnd, colEnd):
    dump = 0
    
    #UL
    if y - 1 < 0 or x - 1 < 0:
        dump += 1
    elif buttons[y - 1][rowEnd + (x - rowEnd) - 1].cget('state') == 'disabled':
        dump += 1
    else:
        buttonClicked(board, buttons[y - 1][rowEnd + (x - rowEnd) - 1], y - 1, rowEnd + (x - rowEnd) - 1)
        if buttons[y - 1][rowEnd + (x - rowEnd) - 1].cget('bg') == 'light grey':
            checkSurrounding(board, buttons, y - 1, rowEnd + (x - rowEnd) - 1, rowEnd, colEnd) 
    #U
    if y - 1 < 0:
        dump += 1
    elif buttons[y - 1][rowEnd + (x - rowEnd)].cget('state') == 'disabled':
        dump += 1
    else:
        buttonClicked(board, buttons[y - 1][rowEnd + (x - rowEnd)], y - 1, rowEnd + (x - rowEnd))
        if buttons[y - 1][rowEnd + (x - rowEnd)].cget('bg') == 'light grey':
            checkSurrounding(board, buttons, y - 1, rowEnd + (x - rowEnd), rowEnd, colEnd) 
    #UR
    if y - 1 < 0 or x + 1 > board.getRowEnd():
        dump += 1
    elif buttons[y - 1][rowEnd + (x - rowEnd) + 1].cget('state') == 'disabled':
        dump += 1
    else:
        buttonClicked(board, buttons[y - 1][rowEnd + (x - rowEnd) + 1], y - 1, rowEnd + (x - rowEnd) + 1)
        if buttons[y - 1][rowEnd + (x - rowEnd) + 1].cget('bg') == 'light grey':
            checkSurrounding(board, buttons, y - 1, rowEnd + (x - rowEnd) + 1, rowEnd, colEnd) 
    #R
    if x + 1 > board.getRowEnd():
        dump += 1
    elif buttons[y][x + 1].cget('state') == 'disabled':
        dump += 1
    else:
        buttonClicked(board, buttons[y][x + 1], y, x + 1)
        if buttons[y][x + 1].cget('bg') == 'light grey':
            checkSurrounding(board, buttons, y, x + 1, rowEnd, colEnd) 
    #BR
    if y + 1 > colEnd or x + 1 > board.getRowEnd():
        dump += 1
    elif buttons[y + 1][rowEnd - (rowEnd - x) + 1].cget('state') == 'disabled':
        dump += 1
    else:
        buttonClicked(board, buttons[y + 1][rowEnd - (rowEnd - x) + 1], y + 1, rowEnd - (rowEnd - x) + 1)
        if buttons[y + 1][rowEnd - (rowEnd - x) + 1].cget('bg') == 'light grey':
            checkSurrounding(board, buttons, y + 1, rowEnd - (rowEnd - x) + 1, rowEnd, colEnd) 
    #B
    if y + 1 > colEnd:
        dump += 1
    elif buttons[y + 1][rowEnd - (rowEnd - x)].cget('state') == 'disabled':
        dump += 1
    else:
        buttonClicked(board, buttons[y + 1][rowEnd - (rowEnd - x)], y + 1, rowEnd - (rowEnd - x))
        if buttons[y + 1][rowEnd - (rowEnd - x)].cget('bg') == 'light grey':
            checkSurrounding(board, buttons, y + 1, rowEnd - (rowEnd - x), rowEnd, colEnd)
    #BL
    if y + 1 > colEnd or x - 1 < 0:
        dump += 1
    elif buttons[y + 1][rowEnd - (rowEnd - x) - 1].cget('state') == 'disabled':
        dump += 1
    else:
        buttonClicked(board, buttons[y + 1][rowEnd - (rowEnd - x) - 1], y + 1, rowEnd - (rowEnd - x) - 1)
        if buttons[y + 1][rowEnd - (rowEnd - x) - 1].cget('bg') == 'light grey':
            checkSurrounding(board, buttons, y + 1, rowEnd - (rowEnd - x) - 1, rowEnd, colEnd)
    #L
    if x - 1 < 0:
        dump += 1
    elif buttons[y][x - 1].cget('state') == 'disabled':
        dump += 1
    else:
        buttonClicked(board, buttons[y][x - 1], y, x - 1)
        if buttons[y][x -1].cget('bg') == 'light grey':
            checkSurrounding(board, buttons, y, x - 1, rowEnd, colEnd) 

def flagSquare(event, board, buttons):
    dump = 0
    x = int((top.winfo_pointerx() - top.winfo_rootx()) / 45)
    y = int(((top.winfo_pointery() - top.winfo_rooty()) / 40) - 0.7)
    #print(y)
    #string = ('x = ' + str(top.winfo_pointerx() - top.winfo_rootx()) + ' y = ' + str(top.winfo_pointery() - top.winfo_rooty()))
    #string = ('x = ' + str(x) + ' y = ' + str(y))
    #print(string)

    #counts number of bombs
    numBombs = 0
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            if buttons[i][j].cget('text') == 'B' or board.fullBoard[i][j] == 'B':
                numBombs += 1

    #print(numBombs)

    #checkWinCond(board, buttons, buttons[y][x], y, x)
    '''
    for i in range(0, 320, 40):
        for j in range(0, 450, 45):
    '''      
            
    #40, 45
    if buttons[y][x].cget('state') == 'disabled':
        dump += 1
    elif (top.winfo_pointery() - top.winfo_rooty()) / 40 <= 0.5:
        #print('hit')
        dump += 1
        w.config(bg = 'yellow')
    elif buttons[y][x].cget('text') == 'F':
        buttons[y][x].config(text = '', fg = 'black', bg = 'SystemButtonFace', image = '', width = 5, height = 2)
    else:
        #print('hit')
        #print((top.winfo_pointery() - top.winfo_rooty()) / 40)
        buttons[y][x].config(text = 'F', fg = 'red', bg = 'yellow', image = photo, width = 38, height = 35)

def clearBoard(buttonList):
    for i in range(len(buttonList)):
        for j in range(len(buttonList[i])):
            buttonList[i][j].destroy()
            #print('hit')

def setDifficulty(checkBox, board, buttonList):
    if checkBox.cget('text') == 'Easy':
        #print('hit')
        boardNew = Minesweeper('Easy')
        #checkMedium.deselect()
        #checkHard.deselect()
        clearBoard(buttonList)
        buttonList.clear()
        checkEasy.grid(column = boardNew.getRowEnd() - 3)
        checkMedium.grid(column = boardNew.getRowEnd() -2)
        checkHard.grid(column = boardNew.getRowEnd())
        start(buttonList, boardNew)
    elif checkBox.cget('text') == 'Medium':
        #print('hit')
        boardNew = Minesweeper('Medium')
        '''checkEasy.deselect()
        checkHard.deselect()'''
        clearBoard(buttonList)
        buttonList.clear()
        checkEasy.grid(column = boardNew.getRowEnd() - 3)
        checkMedium.grid(column = boardNew.getRowEnd() -2)
        checkHard.grid(column = boardNew.getRowEnd())
        start(buttonList, boardNew)
    elif checkBox.cget('text') == 'Hard':
        #print('hit')
        boardNew = Minesweeper('Hard')
        '''checkEasy.deselect()
        checkMedium.deselect()'''
        clearBoard(buttonList)
        buttonList.clear()
        checkEasy.grid(column = boardNew.getRowEnd() - 3)
        checkMedium.grid(column = boardNew.getRowEnd() -2)
        checkHard.grid(column = boardNew.getRowEnd())
        start(buttonList, boardNew)
    else:
        return 'bruh'
    return board

top = tk.Tk()
frame = tk.Frame(top)
top.title('Minesweeper')
frame.grid()
w = tk.Label(top, text = '...')
w.grid(row = 0, column = 0, columnspan = 5)


board = Minesweeper('Easy')

buttonList = []

#making Easy button
checkEasy = tk.Button(top, text = 'Easy')
checkEasy.config(command = partial(setDifficulty, checkEasy, board, buttonList))
checkEasy.grid(row = 0, column = board.getRowEnd() - 3, columnspan = 2)

#making Medium button
checkMedium = tk.Button(top, text = 'Medium')
checkMedium.config(command = partial(setDifficulty, checkMedium, board, buttonList))
checkMedium.grid(row = 0, column = board.getRowEnd() - 2, columnspan = 3)

#making Hard button
checkHard = tk.Button(top, text = 'Hard')
checkHard.config(command = partial(setDifficulty, checkHard, board, buttonList))
checkHard.grid(row = 0, column = board.getRowEnd(), columnspan = 3)

photo = tk.PhotoImage(file = 'flagIMG.png')
#photo = photo.zoom(5)

#x = Toplevel()

def start(buttonList, board):
    for i in range(board.getColEnd() + 1):
        buttonRow = []
        for j in range(board.getRowEnd() + 1):
            b = tk.Button(top, width = 5, height = 2) #width = 40, height = 35
            buttonRow.append(b)
            b.config(command = partial(click, board, b, buttonList, i, j))
            b.grid(row = i + 1, column = j + 1)
            top.bind('<Button-2>', lambda x: flagSquare(x, board, buttonList))
            top.bind('<Button-3>', lambda x: flagSquare(x, board, buttonList))
        buttonList.append(buttonRow)

start(buttonList, board)

top.mainloop()

