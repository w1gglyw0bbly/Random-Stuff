def main():
    display(create_dict(file_read()))

def file_read():
    with open('textStuff.txt', 'r') as x:
        return x.read().split(' ')

def create_dict(txtInput):
    #Removing unnecessary characters from strings and lowering case
    newInput = []
    for x in txtInput:
        if '\n\n' in x:
            for y in range(2):
                newInput.append(x.split('.\n\n')[y].lower())
        elif '.' in x or '\n' in x or ',' in x:
            newInput.append(x.strip(',').strip('.').strip('\n').lower())
        else:
            newInput.append(x.lower())

    #Creating Dictionary
    wordDict = {}
    for x in newInput:
        if x in wordDict:
            wordDict[x] += 1
        else:
            wordDict[x] = 1
    return wordDict

def display(wordDict):
    #Printing words with their count
    print('Word                Frequency\n-------------------------------\n')
    for x in wordDict:
        if wordDict[x] > 1:
            temp = f'{x}'
        else:
            continue
        for y in range(24 - len(x)):
            temp += ' '
        temp += str(wordDict[x])
        print(temp)

    #Printing most common word
    highest = 'python'
    for x in wordDict:
        if wordDict[x] > wordDict[highest]:
            highest = x
    print(f'The most frequent word: {highest}')
        
main()
