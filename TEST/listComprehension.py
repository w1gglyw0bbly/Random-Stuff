import sys

def main():
    sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #newList = [expressoin for item in iterable if condition == True]
    testList = [x * x for x in sampleList]
    print(testList)

main()
