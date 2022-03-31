#-------------------------------------------------------------------------------
# Name: Ronald DeAngelis
# Assignment 3
# Due Date: 2/25/2022
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Zybooks, Prior Knowledge
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

def break_time(hours_worn, last_break):
    total = 0
    #Looping until hours_worn is evenly divisible and returning number of loops
    while 1 == 1:
        if hours_worn % last_break == 0:
            return total
        else:
            hours_worn = int(hours_worn / last_break)
            total += 1

def how_many_uruks(strength_values, init_fund_needed):
    totalUruks = 0
    budget = 0
    #Finding the total budget from the strength_values
    for x in strength_values:
        if x == 0:
            continue
        elif x % 2 != 0:
            budget += x
        else:
            budget *= x

    #Finding totalUruks while the budget is available to buy them
    while init_fund_needed < budget:
        totalUruks += 1
        budget -= init_fund_needed
        init_fund_needed += 1

    return totalUruks

def years_to_rule(n1, n2, n3):
    total = 0
    #Setting up nested loop for n1 and n2
    for x in range(1, n1 + 1):
        for y in range(1, n2 + 1):
            #Adding up years based on calculation instructions
            total += x * y // n3

    return total

def lotr_popularity(char_list):
    popularity = 0
    gandalf, aragorn, legolas = 0, 0, 0
    finalString = ''
    #Looping through characters, totaling popularity and appearance
    for x in char_list:
        if x == 'Gandalf':
            popularity += 10
            gandalf += 1
        elif x == 'Aragorn':
            popularity += 20
            aragorn += 1
        elif x == 'Legolas':
            popularity += 5
            legolas += 1

    #Finding most appeared character
    if gandalf > aragorn and gandalf > legolas:
        finalString = 'Gandalf'
    elif aragorn > legolas and aragorn > gandalf:
        finalString = 'Aragorn'
    else:
        finalString = 'Legolas'

    return f'Most Appeared: {finalString}, Popularity: {popularity}'
