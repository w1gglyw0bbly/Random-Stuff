def main():
    lst = [15, 21, 24, 30, 45]
    lst.sort()
    #print(sieve(lst))
    sieve2(lst)

def sieve(lst):
    singlePrimes = [2, 3, 5, 7]
    nonPrimes = list({y * z for x in lst for y in singlePrimes for z in range(2, int(x / y) + 1)})
    primes = list({y for x in lst for y in range(2, x) if y not in nonPrimes and x % y == 0})
    primes.sort()
    formatPrimes = [[x, sum(y for y in lst if y % x == 0)] for x in primes]
    return formatPrimes

def sieve2(lst):
    singlePrimes = [2, 3, 5, 7]
    nonPrimes = []
    for x in lst:
        i = 2
        if x != lst[0]:
            i = x
        for y in singlePrimes:
            for z in range(i, int(x / y) + 1):
                nonPrimes.append(y * z)
    print(nonPrimes)

main()
