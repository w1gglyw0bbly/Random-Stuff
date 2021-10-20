test = {
    'this' : 1,
    'that' : 2,
    'this' : 3}
'''

        if i in newDict:
            print('hit')
            newDict[dict[i]].append(i)
            continue'''
 
def group_by_owners(dict):
    newDict = {}
    for i in dict:
        if dict[i] in newDict:
            newDict[dict[i]].append(i)
        else:
            newDict.setdefault(dict[i], [i])
    return newDict

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    } 
    print(group_by_owners(files))
