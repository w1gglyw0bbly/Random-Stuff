import requests
from os import getcwd
import os

url = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/test.py?token=AVKQGTPN5TGJM5NA7HOTFIDBKXEXK'
directory = getcwd()
filename = directory + '\\test.py'
print(filename)
r1 = requests.get(url)
r2 = asafdsadsgg



f = open(filename, 'w')
f.write(str(r.content.decode('utf-8')))
f.close()
