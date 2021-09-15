#Testing how to generate a Minesweeper board

import random

'''
testList = [[0, 1, 1, 1, 2, 'B', 3, 1, 0, 0], [0, 1, 'B', 1, 2, 'B', 'B', 1, 0, 0], [0, 1, 1, 1, 1, 2, 3, 2, 1, 0]]


def printBoard(boardList):
    rowLenCount = 0
    
    for i in range(len(boardList)):
        for j in range(len(boardList[i])):
            if i == len(boardList) - 1 and j == len(boardList[i]) - 1:
                print(boardList[i][j])
                
            elif rowLenCount == 10:
                print('\n' + str(boardList[i][j]), end = '')
                rowLenCount = 0
                
            else:
                print(boardList[i][j], end = '')
                
            rowLenCount += 1
    
printBoard(testList)
'''

def inList(parentList, item):
    for i in parentList:
        if item == i:
            return True
    return False

class Minesweeper:

    def __init__(self, diff):
        self.diff = diff
        self.colEnd = self.makeColLen(self.diff)
        self.rowEnd = self.makeRowLen(self.diff)
        self.diffBombNum = self.makeDiffNum(self.diff)
        self.bombs = self.genBombs(self.diffBombNum, self.colEnd, self.rowEnd)
        self.blankBoard = self.generateBlankBoard(self.colEnd, self.rowEnd)
        self.boardWBombs = self.inputBombs(self.blankBoard, self.bombs)
        self.fullBoard = self.inputNums(self.boardWBombs)

    def inputNums(self, boardWBombs):
        for i in range(len(boardWBombs)):
            for j in range(len(boardWBombs[i])):
                boardWBombs[i][j] = self.checkNumber(i, j, boardWBombs)
        fullBoard = boardWBombs
        return fullBoard
    
    def checkUL(self, y, x, boardWBombs):
        if y - 1 < 0 or x - 1 < 0:
            return False
        elif boardWBombs[y - 1][9 + (x - 9) - 1] == 'B':
            return True
        return False

    def checkU(self, y, x, boardWBombs):
        if y - 1 < 0:
            return False
        elif boardWBombs[y - 1][9 + (x - 9)] == 'B':
            return True
        return False

    def checkUR(self, y, x, boardWBombs):
        if y - 1 < 0 or x + 1 > self.rowEnd - 1:
            return False
        elif boardWBombs[y - 1][9 + (x - 9) + 1] == 'B':
            return True
        return False

    def checkR(self, y, x, boardWBombs):
        if x + 1 > self.rowEnd - 1:
            return False
        elif boardWBombs[y][x + 1] == 'B':
            return True
        return False

    def checkBR(self, y, x, boardWBombs):
        if y + 1 > 7 or x + 1 > self.rowEnd - 1:
            return False
        elif boardWBombs[y + 1][9 - (9 - x) + 1] == 'B':
            return True
        return False

    def checkB(self, y, x, boardWBombs):
        if y + 1 > 7:
            return False
        elif boardWBombs[y + 1][9 - (9 - x)] == 'B':
            return True
        return False

    def checkBL(self, y, x, boardWBombs):
        if y + 1 > 7 or x - 1 < 0:
            return False
        elif boardWBombs[y + 1][9 - (9 - x) - 1] == 'B':
            return True
        return False      

    def checkL(self, y, x, boardWBombs):
        if x - 1 < 0:
            return False
        elif boardWBombs[y][x - 1] == 'B':
            return True
        return False

    def checkS(self, y, x, boardWBombs):
        if boardWBombs[y][x] == 'B':
            return True
        return False

    def checkNumber(self, y, x, boardWBombs):
        bombs = 0
        
        if self.checkS(y, x, boardWBombs) == True:
            return 'B'
        if self.checkUL(y, x, boardWBombs) == True:
            bombs += 1
        if self.checkU(y, x, boardWBombs) == True:
            bombs += 1
        if self.checkUR(y, x, boardWBombs) == True:
            bombs += 1
        if self.checkR(y, x, boardWBombs) == True:
            bombs += 1
        if self.checkBR(y, x, boardWBombs) == True:
            bombs += 1
        if self.checkB(y, x, boardWBombs) == True:
            bombs += 1
        if self.checkBL(y, x, boardWBombs) == True:
            bombs += 1
        if self.checkL(y, x, boardWBombs) == True:
            bombs += 1

        return bombs

    def inputBombs(self, blankBoard, bombs):
        for k in range(len(bombs)):
            for i in range(len(blankBoard)):
                for j in range(len(blankBoard[i])):
                    if i == bombs[k][0] and j == bombs[k][1]:
                        blankBoard[i][j] = 'B'
        boardWBombs = blankBoard
        return boardWBombs

    def generateBlankBoard(self, colEnd, rowEnd):
        msBoard = []
        for i in range(colEnd):
            msBoard.append([])
        for i in range(colEnd):
            for j in range(rowEnd):
                msBoard[i].append('')
        return msBoard
    
    def genBombs(self, diffBombNum, colEnd, rowEnd):
        end = diffBombNum
        bombList = []
        for i in range(end):
            while 1 == 1:
                bomb = [random.randint(0, colEnd - 1), random.randint(0, rowEnd - 1)]
                if inList(bombList, bomb) == False:
                    bombList.append(bomb)
                    break
                else:
                    continue
            
        return bombList

    def showBoard(self):
        for i in range(len(self.boardWBombs)):
            print(self.boardWBombs[i])
    
    def makeColLen(self, diff):
        end = 0
        
        if diff == 'Easy':
            end = 8
        elif diff == 'Medium':
            end = 14
        elif diff == 'Hard':
            end = 20
        else:
            print('This is not a valid difficulty')
        return end

    def makeRowLen(self, diff):
        end = 0
        
        if diff == 'Easy':
            end = 10
        elif diff == 'Medium':
            end = 18
        elif diff == 'Hard':
            end = 24
        else:
            print('This is not a valid difficulty')
        return end
    
    def makeDiffNum(self, diff):
        end = 0
        
        if diff == 'Easy':
            end = 10
        elif diff == 'Medium':
            end = 40
        elif diff == 'Hard':
            end = 99
        else:
            print('This is not a valid difficulty')
        return end


    #Accessors
    def getBombs(self):
        return self.bombs

    def getDiff():
        return self.diff

    #Modifiers
    def setBombs(): 
        self.bombs = self.genBombs(self.diff)

    def setDiff(self, diff):
        self.diff = diff

    def setBlankBoard():
        self.blankBoard = self.generateBlankBoard(self.colEnd, self.rowEnd)

    def newFullBoard(self):
        self.fullBoard = self.inputNums(self.inputBombs(self.generateBlankBoard(self.colEnd, self.rowEnd), self.genBombs(self.diffBombNum, self.colEnd, self.rowEnd)))
        print(self.fullBoard)
        

#Testing Class Objects and Stuff

test = Minesweeper('Easy')

print('test: ' + str(test.fullBoard))
print('test2: ')
test.newFullBoard()
