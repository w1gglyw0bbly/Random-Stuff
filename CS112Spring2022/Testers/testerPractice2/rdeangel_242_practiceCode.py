def inchestoFtYards(user_input):
	num = int(user_input/12)
	yards = int(num/3)
	inches = user_input%12
	feet = num%3
	result = "That is: \n"  + str(yards) + " yards, " + str(feet) + " feet " + str(inches) + " inches."
	return result
