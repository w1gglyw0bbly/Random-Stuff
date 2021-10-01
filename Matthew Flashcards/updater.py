import requests
from os import getcwd
import subprocess
import sys
import urllib.request
import os
import urllib.request

#url = 'https://github.com/w1gglyw0bbly/Random-Stuff/blob/main/Matthew%20Flashcards/bruh'
url = 'https://github.com/w1gglyw0bbly/Random-Stuff/blob/main/Matthew%20Flashcards/dist/updater.exe'
#urllib.request.urlretrieve(url, 'D:\Github Repositories\Random-Stuff\Matthew Flashcards\\bruh.txt')
urllib.request.urlretrieve(url, 'D:\Github Repositories\Random-Stuff\Matthew Flashcards\\test\\test.exe')

urlTest = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/test.py?token=AVKQGTPN5TGJM5NA7HOTFIDBKXEXK'
urlVersion = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/appInfo.txt'
urlMain = 'https://github.com/w1gglyw0bbly/Random-Stuff/raw/main/Matthew%20Flashcards/dist/main.exe'

directory = getcwd()
filenameTest = os.path.join(directory, 'test.py')
filenameAppInfo = os.path.join(directory, 'appInfo.txt')
filenameMain = os.path.join(directory, 'main.exe')
#filenameMain = os.path.join(directory, 'dist/main.exe')
print(filenameTest)
rTest = requests.get(urlTest)
rVersion = requests.get(urlVersion)
rMain = requests.get(urlMain)

f = open(filenameAppInfo, 'r')
localText = f.read().split(':')[1]
repoText = str(rVersion.content.decode('utf-8')).split(':')[1]
#print(text)
#print(str(rVersion.content.decode('utf-8')).split(':')[1])
print(repoText)
if localText == repoText:
    subprocess.run('main.exe')
    #subprocess.run('dist/main.exe')
    print('cum')
else:
    urllib.request.urlretrieve(urlMain, filenameMain)
    '''
    f = open(filenameMain, 'w')
    f.write(str(rMain.content))
    f.close()
    '''
f = open(filenameTest, 'w')
f.write(str(rTest.content.decode('utf-8')))
f.close()
