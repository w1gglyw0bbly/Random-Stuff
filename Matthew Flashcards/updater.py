import requests
from os import getcwd
import os

urlTest = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/test.py?token=AVKQGTPN5TGJM5NA7HOTFIDBKXEXK'
urlVersion = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/appInfo.txt'
urlMain = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/airplaneFlashCards.py'

directory = getcwd()
filenameTest = directory + '\\test.py'
filenameAppInfo = directory + '\\appInfo.txt'
filenameMain = directory + '\\airplaneFlashCards.py'
print(filenameTest)
rTest = requests.get(urlTest)
rVersion = requests.get(urlVersion)
rMain = requests.get(urlMain)

f = open(filenameAppInfo, 'r')
localText = f.read().split(':')[1]
repoText = str(rVersion.content.decode('utf-8')).split(':')[1]
#print(text)
#print(str(rVersion.content.decode('utf-8')).split(':')[1])
if localText == repoText:
    os.system('airplaneFlashCards.py')
else:
    f = open(filenameMain, 'w')
    f.write(str(rMain.content.decode('utf-8')))
    f.close()


f = open(filenameTest, 'w')
f.write(str(rTest.content.decode('utf-8')))
f.close()
