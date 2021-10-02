import requests
from os import getcwd
import subprocess
import urllib.request
import os

directory = getcwd()
urlVersion = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/appInfo.txt'
urlUpdater = 'https://github.com/w1gglyw0bbly/Random-Stuff/raw/main/Matthew%20Flashcards/dist/updater.exe'
filenameAppInfo = os.path.join(directory, 'appInfo.txt')
filenameUpdater = os.path.join(directory, 'updater.exe')
rVersion = requests.get(urlVersion)
f = open(filenameAppInfo, 'r')
localText = f.read().split(':')[3]
#print(localText)
repoText = str(rVersion.content.decode('utf-8')).split(':')[3]

if localText == repoText:
    subprocess.run('updater.exe')
else:
    urllib.request.urlretrieve(urlUpdater, filenameUpdater)
    subprocess.run('updater.exe')
    
