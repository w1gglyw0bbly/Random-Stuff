firstWord, secondWord, cipherText = 'monkeys', 'zebras', 'ADDDFDDAXFXAGGFDXXAXFGXFGG'
board5x5 = ['A', 'D', 'F', 'G', 'X']
board6x6 = ['A', 'D', 'F', 'G', 'V', 'X']
s1 = 'abc'
s2 = 'def'
'''
{x:y for (x, y) in zip(alphabet, alphabet[::-1])}
lst = [(j, k) for j in s1 for k in s2]
print(lst)'''

def makeEncryptedBoard(secondWord, cipherText):
    secondWord = list(secondWord)
    secondWord.sort()
    #print(secondWord)
    encryptedBoard = [[x for x in secondWord], [y for i in range(5) for y in range(1,6)]]
    print(encryptedBoard)
    
    
    


makeEncryptedBoard(secondWord, cipherText)
#if cipherText <= 25:

str1 = 'edwhrkieuwiiornnrthstooogthofhdrwiotsifss' 
str2 = 'hssthelaaenchamllnwoleniesdhtothndeeohsr'


