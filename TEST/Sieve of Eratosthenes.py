def main():
    primes = sieve(200)
    print(primes)



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

def getPrimes(nonPrimes, end):
    end += 1
    primes = []
    for y in range(2, end):
        if y not in nonPrimes:
            primes.append(y)
    return primes

main()
