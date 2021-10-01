import requests
import urllib.request
from tkinter import filedialog as fd
from tkinter import *
import tkinter as tk
import partial

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

def yourMom():
    

def bruh(b):
    #test = fd.askopenfilename()
    filename.setFilename(fd.askopenfilename())
    print(filename.getFilename())
    #print('bruh ' + test)
    b.config(text = 'Install', command = yourMom)

b = tk.Button(test, text = 'fuck you')
b.config(command = partial(bruh, b))
test.pack()
b.grid(row = 0, column = 0, pady = 20)


#root.destroy()
tk.mainloop()


