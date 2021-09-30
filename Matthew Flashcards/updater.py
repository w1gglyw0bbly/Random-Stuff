import requests
from os import getcwd
import os

urlTest = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/test.py?token=AVKQGTPN5TGJM5NA7HOTFIDBKXEXK'
urlVersion = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/appInfo.txt'

directory = getcwd()
filenameTest = directory + '\\test.py'
filenameAppInfo = directory + '\\appInfo.txt'
print(filenameTest)
rTest = requests.get(urlTest)
rVersion = requests.get(urlVersion)

f = open(filenameAppInfo, 'r')
text = f.read().split(':')[1]
print(text)
print(str(rVersion.content.decode('utf-8')).split(':')[1])


f = open(filenameTest, 'w')
f.write(str(rTest.content.decode('utf-8')))
f.close()
