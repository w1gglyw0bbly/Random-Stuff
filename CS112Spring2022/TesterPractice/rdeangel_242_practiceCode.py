user_input = int(input("Please enter a measurement in inches: "))
num = int(user_input/12)
yards = int(num/3)
inches = user_input%12
feet = num%3
print("That is: \n"  + str(yards) + " yards, " + str(feet) + " feet, " + str(inches) + " inches.")

