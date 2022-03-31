def stones_to_drams(stones):
    return stones * 3583.99

def approximator(N):
    nums10 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #Checks if N is equal to the word from nums10 based on index
    for x in range(len(nums10)):
        if N == x + 1:
            return nums10[x]
    #If nothing in the list works it must be greater so it returns lots
    return 'lots'

def multiplier(lst, N):
    #Loops through list and multiplies each item by N
    for x in range(len(lst)):
        lst[x] = lst[x] * N
    return lst

