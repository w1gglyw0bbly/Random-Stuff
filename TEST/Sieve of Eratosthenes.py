def main():
    primes = sieve2(120)
    print(primes)

s = {s for s in [1,2,3] if s % 2 != 0}
print(s)

def sieve(end):
    end += 1
    singlePrimes = [2, 3, 5, 7]
    nonPrimes = []
    primes = []
    for x in singlePrimes:
        for y in range(2, int(end/x)+1):
            if x * y in nonPrimes:
                continue
            nonPrimes.append(x * y)
    for x in range(2, end):
        if x not in nonPrimes:
            primes.append(x)
    return primes

def sieve2(end):
    end += 1
    singlePrimes = [2, 3, 5, 7]
    #nonPrimes = [x * y for x in singlePrimes for y in range(2, int(end/x)+1) if x * y not in this.nonPrimes]
    #primes = [x for x in range(2, end) if x not in nonPrimes]
    return 0

'''
def getPrimes(nonPrimes, end):
    end += 1
    primes = []
    for y in range(2, end):
        if y not in nonPrimes:
            primes.append(y)
    return primes
'''

main()
