import requests
from os import getcwd

url = 'https://raw.githubusercontent.com/w1gglyw0bbly/Random-Stuff/main/Matthew%20Flashcards/test.py?token=AVKQGTPN5TGJM5NA7HOTFIDBKXEXK'
directory = getcwd()
filename = directory + '\\test.py'
print(filename)
r = requests.get(url)

f = open(filename, 'w')
f.write(str(r.content.decode('utf-8')))
f.close()
