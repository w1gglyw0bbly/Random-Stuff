side1 = int(input('Length of side 1'))
side2 = int(input('Length of side 2'))
side3 = int(input('Length of side 3'))

#swaps sides so side1 ends up as the largest to test pythagorean theorem correctly
if side3 > side2:
    tempSide = side2
    side2 = side3
    side3 = tempSide

if side2 > side1:
    tempSide = side1
    side1 = side2
    side2 = tempSide

if (side1 * side1 == side2 * side2 + side3 * side3):
    print('It is a right triangle')
else:
    print('It is not a right triangle')

def isRightTriangle(side1, side2, side3):
    if side3> side2:
        tempSide = side2
        side2 = side3
        side3 = tempSide

    if side2 > side1:
        tempSide = side1
        side1 = side2
        side2 = tempSide

    if(side1 * side1 == side2 * side2 + side3 * side3):
        result = 'It is a right triangle'
    else:
        result = 'It is not a right triangle'

    return result
