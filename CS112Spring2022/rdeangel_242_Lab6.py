def calcAverage(data_dictionary):
    total = 0
    avg_dictionary = {}
    #Loops through keys
    for x in data_dictionary:
        #Loops through list of grades
        for y in range(len(data_dictionary[x])):
            #Sums up grades
            total += data_dictionary[x][y]
        #Adds grade average and student name to new dict
        avg_dictionary[x] = round(total / len(data_dictionary[x]), 2)
        total = 0
    return avg_dictionary
