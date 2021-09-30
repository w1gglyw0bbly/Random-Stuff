import requests
from os import getcwd

url = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/airplaneFlashCards.py?token=AVKQGTIVD2HTCWI7EJB744DBKXEH6'
directory = getcwd()
filename = directory + 'test.py'
r = requests.get(url)

f = open(filename, 'w')
f.write(r.content)
