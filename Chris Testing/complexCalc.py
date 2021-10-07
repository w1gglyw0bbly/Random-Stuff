a1, b1, a2, b2 = 0, 0, 0, 0
numInputs = [a1, b1, a2, b2]
log = []

def start():
    menuChoice = int(input('1) Equality\n2) Addition\n3) Subtraction\n4) Multiplication\n5) Exit\nEnter choice (from 1-5): '))
    return menuChoice

def getInputs():
    numInputs[0] = int(input('Enter a1: '))
    numInputs[1] = int(input('Enter b1: '))
    numInputs[2] = int(input('Enter a2: '))
    numInputs[3] = int(input('Enter b2: '))

def equality():
    if numInputs[0] == numInputs[2] and numInputs[1] == numInputs[3]:
        output = f'({numInputs[0]} - i{numInputs[1]}) = ({numInputs[2]} - i{numInputs[3]})'
        log.append(output)
        return output
    else:
        return "bro you wildin'"

def addition():
    output = f'({numInputs[0]} - i{numInputs[1]}) + ({numInputs[2]} - i{numInputs[3]}) = {numInputs[0] + numInputs[2]} - i{numInputs[1] + numInputs[3]}'
    log.append(output)
    return output
    
def subtraction():
    if numInputs[1] - numInputs[3] < 0:
        output = f'({numInputs[0]} - i{numInputs[1]}) - ({numInputs[2]} - i{numInputs[3]}) = {numInputs[0] - numInputs[2]} + i{abs(numInputs[1] - numInputs[3])}'
        log.append(output)
        return output
    else:
        output = f'({numInputs[0]} - i{numInputs[1]}) - ({numInputs[2]} - i{numInputs[3]}) = {numInputs[0] - numInputs[2]} - i{numInputs[1] - numInputs[3]}'
        log.append(output)
        return output

def multiplication():
    if (numInputs[0] * -numInputs[3]) + (-numInputs[1] * numInputs[2]) < 0:
        output = f'({numInputs[0]} - i{numInputs[1]}) * ({numInputs[2]} - i{numInputs[3]}) = {numInputs[0] * numInputs[2] - numInputs[1] * numInputs[3]} - i{abs(numInputs[0] * numInputs[3] + numInputs[1] * numInputs[2])}'
        log.append(output)
        return output
    else:
        output = f'({numInputs[0]} - i{numInputs[1]}) * ({numInputs[2]} - i{numInputs[3]}) = {numInputs[0] * numInputs[2] - numInputs[1] * numInputs[3]} + i{numInputs[0] * numInputs[3] + numInputs[1] * numInputs[2]}'
        log.append(output)
        return output

def exit():
    print('************* Printing Logs *************')
    for x in log:
        print(x)
    print('Exiting application')

def calc():
    menuChoice = start()
    #print(menuChoice)
    if isinstance(menuChoice, int) == True and menuChoice != 5:
        getInputs()
        #print(f'{numInputs[0]} {numInputs[1]} {numInputs[2]} {numInputs[3]}')
        if menuChoice == 1:
            print(f'{equality()}\n')
            calc()
        if menuChoice == 2:
            print(f'{addition()}\n')
            calc()
        if menuChoice == 3:
            print(f'{subtraction()}\n')
            calc()
        if menuChoice == 4:
            print(f'{multiplication()}\n')
            calc()
    elif menuChoice == 5:
        exit()
        return 'your mom'
    else:
        return 'bro how though'




calc()
    


