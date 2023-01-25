def split_in_half(vals):
    firstHalf = []
    secondHalf = []
    for x in range(int(len(vals) / 2)):
        firstHalf.append(vals[x])
    for z in range(int(len(vals) / 2), len(vals)):
        secondHalf.append(vals[z])
    return [firstHalf, secondHalf]

def even_odd(tups):
    tupleDict = {'odd' : 0,
                 'even' : 0}
    for x in tups:
        if len(x) % 2 == 0:
            tupleDict['even'] += 1
        elif len(x) % 2 != 0:
            tupleDict['odd'] += 1
    return tupleDict

def contains_ints(tocheck):
    check = False
    for x in tocheck:
        try:
            x = x + 1
            return True
        except:
            check = False
    return False
            
