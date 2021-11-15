def main():
    findP([12, 15])

def findP(lst):
    lst.sort()
    primes, final = [2], []
    for x in range(3, lst[len(lst) - 1], 2):
        print(x)
        if checkDivis(x, primes) != True:
            summing = 0
            for y in lst:
                if x not in primes and checkDivis(y, primes) != True:
                    primes.append(x)
                if checkDivis(y, primes) == True and x in primes:
                    summing += y
            if summing != 0:
                print('hit')
                final.append([x, summing])
    print(primes)
    print(final)

def checkDivis(var, lst):
    for x in lst:
        if var % x == 0:
            return True
    return False

main()
