def main():
    print('pussy')
    size = getInput()
    print(f'Size: {size}')

def getInput():
    size = input('Enter the number of trucks between 2 and 10: ')
    while size < 2 or size > 10:
        print('That is not a valid entry, the evaluation must contain between 2 and 10 vehicles')
        size = input('Enter the number of trucks between 2 and 10: ')
    return size




main()
