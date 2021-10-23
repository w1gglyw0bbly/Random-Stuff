import time
start = time.process_time()
lst = list('bruh')
###
def sum_for_list(lst):
    x=0
    lstPos = [x := x * -1 if x < 0 else x]
    return sieve(lst, lstPos)
    
def sieve(lst, lstPos):
    singlePrimes = [2, 3, 5, 7]
    formatPrimes, primes, nonPrimes = [], [], []
    nonPrimes = [y * z for x in lst for y in singlePrimes for z in range(2, int(x / y) + 1) if y * z not in nonPrimes]
    
    for x in lst:
        for y in range(2, x):
            if y not in nonPrimes and y not in primes and x % y == 0:
                primes.append(y)
    primes.sort()
    #Formatting Primes List
    for x in primes:
        sum = 0
        for y in lst:
            if y % x == 0:
                sum += y
        formatPrimes.append([x, sum])
    return formatPrimes
###
#finalList = [[x for x in lst], [x for x in range(1, 6)] for y in range(5)]
#finalList = [[y for y in range(1, 6)] for x in range(5), [x for x in lst]]
#print(finalList)

print(sum_for_list([12, 15]))

print(time.process_time() - start)
