#Get year input from user
year = int(input('Enter the year on the document:\n'))

#Check if dividing by 4 has remainder and if 100 doesn't
if year % 4 == 0 and year % 100 != 0:
    print('Real document')
#Check if 400 has remainder
elif year % 400 == 0:
    print('Real document')
#If neither of previous it is false
else:
    print('Forged document')

#Optional Question
print() #For readability in output
daysLate = int(input('Enter the number of late days:\n'))
membership = int(input('Enter the membership status (1 = member, 0 = non-member):\n'))
originalPrice = int(input('Enter the original price of the book:\n'))
totalFine = 0

if membership == 1:
    if daysLate // 10 > 0:
        totalFine += 10 * .25
    if daysLate // 20 > 0:
        totalFine += 10 * .5
    if daysLate > 20:
        totalFine += (daysLate - 20) * .75
    totalFine -= totalFine * .2
    if totalFine > originalPrice * 2:
        totalFine = originalPrice * 2
else:
    if daysLate // 10 > 0:
        totalFine += 10 * .25
    if daysLate // 20 > 0:
        totalFine += 10 * .5
    if daysLate > 20:
        totalFine += (daysLate - 20) * .75
    if totalFine > originalPrice * 2:
        totalFine = originalPrice * 2

print(f'${int(totalFine)}')
