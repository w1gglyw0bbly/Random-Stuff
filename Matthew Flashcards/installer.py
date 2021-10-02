import requests
import urllib.request
from tkinter import filedialog as fd
from tkinter import *
import tkinter as tk
from functools import partial
import os

root = Tk()
test = tk.Frame(root)

class Directory:
    def __init__(self, filename):
        self.filename = filename

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename


filename = Directory('')

def end():
    root.destroy()

def yourMom(b):
    urlMain = 'https://github.com/w1gglyw0bbly/Random-Stuff/raw/main/Matthew%20Flashcards/dist/main.exe'
    urlUpdater = 'https://github.com/w1gglyw0bbly/Random-Stuff/raw/main/Matthew%20Flashcards/dist/updater.exe'
    urlVersionInfo = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/dist/appInfo.txt'
    urlLauncher = 'https://github.com/w1gglyw0bbly/Random-Stuff/raw/main/Matthew%20Flashcards/dist/installer.exe'
    urllib.request.urlretrieve(urlMain, os.path.join(filename.getFilename(), 'main.exe'))
    urllib.request.urlretrieve(urlUpdater, os.path.join(filename.getFilename(), 'updater.exe'))
    urllib.request.urlretrieve(urlVersionInfo, os.path.join(filename.getFilename(), 'appInfo.txt'))
    urllib.request.urlretrieve(urlLauncher, os.path.join(filename.getFilename(), 'launcher.exe'))
    b.config(text = 'Done', command = end)

def bruh(b):
    #test = fd.askopenfilename()
    filename.setFilename(fd.askdirectory())
    print(filename.getFilename())
    #print('bruh ' + test)
    b.config(text = 'Install', command = partial(yourMom, b))

b = tk.Button(test, text = 'fuck you')
b.config(command = partial(bruh, b))
test.pack()
b.grid(row = 0, column = 0, pady = 20)


#root.destroy()
tk.mainloop()


