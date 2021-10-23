#Hello to JDMJQ
def main():
    key = ['n+2', 'n-1', 'n+1', 'n-2']
    print(encrypt(key, phrase := input('Type word to be encoded: ')))
    
def encrypt(key, phrase):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = ''
    for x in phrase:
        for y in key:
            answer += encryptLetter(alpha, phrase, x, y)
    return 'your mom'

def encryptLetter(alpha, phrase, num, y):
    stuff = [y.split('+') if '+' in y else y.split('-')]
    print(stuff)
    if '+' in y:
        return alpha.index(num) + stuff[1]
    else:
        return alpha.index(num) - stuff[1]
main()

#Easy
#GXTW
