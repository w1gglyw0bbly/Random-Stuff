anne = 0
count = 0
while count < 5:
    cost = int(input('Input Cost: '))
    while cost < 0:
        cost = int(input('Input Cost: '))
    anne += cost
    count += 1
gigi = 0
count = 0
while count < 5:
    cost = int(input('Input Cost: '))
    while cost < 0:
        cost = int(input('Input Cost: '))
    gigi += cost
    count += 1
if gigi < anne:
    print('Gigi: ' + str(gigi))
else:
    print('Anne: ' + str(anne))
