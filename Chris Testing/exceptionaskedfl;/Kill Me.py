def summation(sequence):
    total_sum = 0
    for s in sequence:
        try:
            total_sum += float(s)
        except:
            print('Not a number, continue to next element')
            continue
    return total_sum

def reciprocal(n):
    try:
        return 1/float(n)
    except:
        return 'Zero and string not allowed'

def getList(filename):
    try:
        f = open(filename)
        temp = f.readline()
        return [t.split('\n')[0] for t in temp.split(',')]
    except:
        return False

def main():
    sequence = getList('AAAAAA.txt')
    if sequence == False:
        print('File I/O error')
    else:
        print('The sequence is: ', sequence)

        print('**** Calculating Summation ****')
        print(summation(sequence))

        print('**** Calculating Reciprocal ****')
        for s in sequence:
            print('{}: {}'.format(s, reciprocal(s)))

main()
