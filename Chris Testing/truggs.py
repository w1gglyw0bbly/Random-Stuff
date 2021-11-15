import random as r

def main():
    size = getInput()
    trucks = makeDict(size)
    print('\nThe trucks and their speeds')
    for x in trucks:
        print(f'{x}:', end = ' ')
        for y in trucks[x]:
            if y != trucks[x][2]:
                print(f'{y}mph, ', end = '')
            else:
                print(f'{y}mph')
    indAvgs = calcAvgInd(trucks)
    print('\nIndividual speed averages')
    for x in indAvgs:
        print(f'{x}: {indAvgs[x]}mph')
    print(f'\nFastest Car:\n{getHighest(indAvgs)[0]} - {getHighest(indAvgs)[1]}mph\n')
    print(f'Slowest Car:\n{getLowest(indAvgs)[0]} - {getLowest(indAvgs)[1]}mph\n')
    print(f'Overall Average Speed: {calcAvgTotal(indAvgs)}mph')


def getInput():
    size = int(input('Enter the number of trucks between 2 and 10: '))
    print()
    while size < 2 or size > 10:
        print('That is not a valid entry, the evaluation must contain between 2 and 10 vehicles')
        size = int(input('Enter the number of trucks between 2 and 10: '))
        print()
    return size

def makeDict(size):
    trucks = {}
    for x in range(size):
        name = input(f'Enter the name of truck {x + 1}: ')
        trucks[name] = []
    trucks = generateSpeeds(trucks)
    return trucks

def generateSpeeds(trucks):
    speeds = []
    for x in trucks:
        temp = []
        for y in range(3):
            temp.append(r.randint(1, 50))
        trucks[x] = temp
    return trucks

def calcAvgInd(trucks):
    indAvgs = {}
    for x in trucks:
        total = 0
        for y in trucks[x]:
            total += y
        indAvgs[x] = round(total / 3)
    return indAvgs

def calcAvgTotal(indAvgs):
    total = 0
    for x in indAvgs:
        total += indAvgs[x]
    return round(total / len(indAvgs))

def getHighest(indAvgs):
    highest = ('', 0)
    for x in indAvgs:
        if indAvgs[x] > highest[1]:
            highest = (x, indAvgs[x])
    return highest

def getLowest(indAvgs):
    highest = ('', 0)
    position = 0
    for x in indAvgs:
        if position == 0:
            lowest = (x, indAvgs[x])
            position += 1
        elif indAvgs[x] < lowest[1]:
            lowest = (x, indAvgs[x])
            position += 1
    return lowest
            

if __name__ == '__main__':
    main()
