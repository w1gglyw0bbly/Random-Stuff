import requests
from os import getcwd
import subprocess
import sys
import urllib.request

#url = 'https://github.com/w1gglyw0bbly/Random-Stuff/blob/main/Matthew%20Flashcards/bruh'
url = 'https://github.com/w1gglyw0bbly/Random-Stuff/blob/main/Matthew%20Flashcards/dist/updater.exe'
#urllib.request.urlretrieve(url, 'D:\Github Repositories\Random-Stuff\Matthew Flashcards\\bruh.txt')
urllib.request.urlretrieve(url, 'D:\Github Repositories\Random-Stuff\Matthew Flashcards\\test\\test.exe')

urlTest = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/test.py?token=AVKQGTPN5TGJM5NA7HOTFIDBKXEXK'
urlVersion = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/appInfo.txt'
urlMain = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/airplaneFlashCards.py'

directory = getcwd()
filenameTest = directory + '\\test.py'
filenameAppInfo = directory + '\\appInfo.txt'
filenameMain = directory + '\\airplaneFlashCards.pyw'
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
    subprocess.run('airplaneFlashCards.pyw')
    print('cum')
else:
    f = open(filenameMain, 'w')
    f.write(str(rMain.content.decode('utf-8')))
    f.close()


f = open(filenameTest, 'w')
f.write(str(rTest.content.decode('utf-8')))
f.close()
