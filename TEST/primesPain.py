def main():
    findP(120)

def findP(max):
    primes = []
    for x in range(2, max + 1):
        if checkDivis(x, primes) != True:
            primes.append(x)
    print(primes)

def checkDivis(var, lst):
    if len(lst) == 0:
        return False
    for x in lst:
        if var % x == 0:
            return True
    return False

main()
