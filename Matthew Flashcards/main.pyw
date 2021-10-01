from tkinter import *
import tkinter as tk
from functools import partial
from tkinter.ttk import *
import os
import random
import sys


root = tk.Tk()
test = tk.Frame(root)
check = tk.IntVar()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


with open(resource_path('data.txt'), 'r') as x:
    qAndA = x.readlines()

def hideButton(button, q):
    button.grid_forget()
    q.grid(row = 0, column = 1, pady = 10, ipadx = 5, ipady = 2)
    for i in qAndA:
        print(i)

def continueB(answer, check, nextB):
    check.set(1)
    nextB.grid_forget()
    answer.grid(row = 1, column = 0)
    

def showAnswer(answer, check, q, item):
    #print('pog')
    #print(item.split(':')[1])
    q.config(text = item.split(':')[4] + '\n' + item.split(':')[0] + '\n------------------------------ Answer -------------------------------\n' + item.split(':')[1] + '\n' + item.split(':')[2] + ':' + item.split(':')[3])
    answer.grid_forget()
    #nextB = tk.Button(test, text = 'Next Question')
    nextB.config(command = partial(continueB, answer, check, nextB))
    nextB.grid(row = 1, column = 0)
    #root.update()
    

def showQuestions(startB, exitB, q):

    startB.grid_forget()
    exitB.grid(pady = (20, 0), row = 2)
    #answer = tk.Button(test, text = 'Answer')
    answer.grid(row = 1, column = 0)
    currentQs = qAndA
    for i in range(len(currentQs)):
        index = random.randint(0, len(currentQs) - 1)
        #print(len(currentQs))
        #print('length: ' + str(i) + ' index: ' + str(index))
        q.config(text = currentQs[index].split(':')[4] + '\n' + currentQs[index].split(':')[0])
        q.grid(row = 0, column = 0)
        answer.config(command = partial(showAnswer, answer, check, q, currentQs[index]))
        currentQs.pop(index)
        q.wait_variable(check)
        '''while check == True:
            print('fuck')'''

def end():
    check.set(check.get())
    root.destroy()



'''Making labels'''
#Question Label
question = tk.Label(test, text = '', relief = 'solid', wraplength = 500)
question.grid(padx = 50, pady = 15, ipadx = 5, ipady = 2)
question.forget()

'''Making buttons w/ commands'''
#Exit Button
exitB = tk.Button(test, text = 'Exit')
exitB.config(command = end)
exitB.grid(row = 1, column = 0)

#Start Button
start = tk.Button(test, text = 'Start')
#start.config(command = partial(hideButton, start, question))
start.config(command = partial(showQuestions, start, exitB, question))
start.grid(row = 0, column = 0, pady = 10)



answer = tk.Button(test, text = 'Answer')
#answer.config(command = partial(showAnswer, answer, check, q, i))

nextB = tk.Button(test, text = 'Next Question')
#nextB.config(command = partial(continueB, check, nextB))

#packing
test.pack()

#loop bruh
root.mainloop()

sys.exit()
