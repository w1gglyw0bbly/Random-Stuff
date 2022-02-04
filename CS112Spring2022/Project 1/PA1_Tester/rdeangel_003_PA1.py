print('Sage\'s Wedding Cake Price Calculator') #Printing header for program
people = int(input('Total People Attending: ')) #Getting user input for # of people attending

#Getting a base price to use for each cake type, consisting of the labor cost
cakeABase = (15 * 15) + 12.5
cakeBBase = (15 * 14) + (12.5 * 2)
cakeCBase = (15 * 16) + (12.5 * 1.5)

print('----------------------------------------')
print('Cake A')
print('Labor Cost:     \t$' + str(round(cakeABase * (people / 30), 2))) #Printing labor cost for for cake A and adding the extra cost for number of cakes
print('Cost to Make:   \t$' + str(round((cakeABase + 35) * (people / 30), 2))) #Printing cost to make for cake A which adds the base for ingredients
print('Charge Customer: \t$' + str(round((cakeABase + 35) * (people / 30) + ((cakeABase + 35) * (people / 30) * .1), 2))) #Printing customer charge for cake A including the 10% profit for the bakery
#The three above comments for cake A apply for the next two cakes as well
print('----------------------------------------')
print('Cake B')
print('Labor Cost:     \t$' + str(round(cakeBBase * (people / 30), 2)))
print('Cost to Make:   \t$' + str(round((cakeBBase + 30) * (people / 30), 2)))
print('Charge Customer: \t$' + str(round((cakeBBase + 30) * (people / 30) + ((cakeBBase + 30) * (people / 30) * .1), 2)))
print('----------------------------------------')
print('Cake C')
print('Labor Cost:     \t$' + str(round(cakeCBase * (people / 30), 2)))
print('Cost to Make:   \t$' + str(round((cakeCBase + 40) * (people / 30), 2)))
print('Charge Customer: \t$' + str(round((cakeCBase + 40) * (people / 30) + ((cakeCBase + 40) * (people / 30) * .1), 2)))
