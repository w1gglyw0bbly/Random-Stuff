def make_format_str(num_reps, num_vals):
    fstr = ''
    for x in range(num_reps):
        for y in range(num_vals):
            if x == num_reps - 1 and num_reps != 1:
                fstr += '{' + str(y) + '}'
            else:
                fstr += '{' + str(y) + '} '
    return fstr

#test = make_format_str(1, 2)
#print(test.format('Hello!', 'World!'))


def lucas_number(n):
    total = 0
    seriesStart = [2,1]
    if n == 0:
        return 2
    elif n == 1:
        return 1
    for x in range(n + 1):
        if x > 1:
            seriesStart.append(seriesStart[x - 1] + seriesStart[x - 2])
    total = seriesStart[x]
    return total

#print(lucas_number(2))

def int_log2(x):
    powerNum = 2
    powerCount = 1
    for y in range(x):
        if powerNum == x:
            return powerCount
        if powerNum > x:
            #raise Exception('ValueError: x is not a multiple of 2')
            return 'ValueError: x is not a multiple of 2'
        else:
            powerNum *= 2
            powerCount += 1
    return powerCount

#print(int_log2(65))

