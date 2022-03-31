#Part 1
def calcSum(number):
    result = 0
    for x in range(number):
        result += x
    return result

#Part 2
def calcList(number_list):
    tempList = []
    result = 1
    #Looping through list items
    for x in number_list:
        tempList.append(calcSum(x))
        
    #Multiply added numbers
    for z in tempList:
        result *= z
    return result
