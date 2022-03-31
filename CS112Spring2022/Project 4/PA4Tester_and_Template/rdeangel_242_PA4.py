#-------------------------------------------------------------------------------
# Name: Ronald DeAngelis
# Assignment 4
# Due Date: 3/14/2022
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: zybooks and past knowledge
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

def biggest_vertebrate(animals, weights, vertebrates):
    weightHighest = 0
    indexHighest = -1
    #Returns None if animals list is empty
    if len(animals) == 0:
        return None
    for x in range(len(animals)):
        for y in range(len(vertebrates)):
            #Changes the highest weight and index if bigger vertebrate is found
            if animals[x] == vertebrates[y] and weights[x] > weightHighest:
                weightHighest = weights[x]
                indexHighest = x
                break
    #Returns correct list as long as there are vertebrates in animals list
    if indexHighest != -1:
        return animals[indexHighest]
    #Return None for there being no vertebrates in animals list
    return None

def within_weight(animals, weights, weightLimit):
    withinWeightAnimals = []
    for x in range(len(animals)):
        if weights[x] <= weightLimit:
            withinWeightAnimals.append(animals[x])
    return withinWeightAnimals

def any_adjacent_vertebrates(animals, vertebrates):
    for x in range(len(animals)):
        for y in vertebrates:
          #Checks if current animal is vertebrate and not last item in the list
            if animals[x] == y and x != len(animals) - 1:
                for z in vertebrates:
                    #Checks if animal ahead (next to) is vertebrate
                    if animals[x + 1] == z:
                        return True
    return False              

def count_weights(weight_list):
    total = 0
    for x in range(len(weight_list)):
        for y in range(len(weight_list)):
            #Stops repeating used combinations
            if y <= x:
                continue
            #Variable for ease of use
            sumN = weight_list[x] + weight_list[y]
            for z in weight_list:
                #Checks if sum is in the list
                if sumN == z:
                    total += 1
                    break
    return total
