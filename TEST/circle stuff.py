import turtle as t
import random
t.hideturtle()

def genCoords(): 
    return (random.randint(-100, 100), random.randint(-100, 100))

def drawCircle(radius):
    t.circle(radius)
    t.up()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.down()
    t.color('green')
    t.circle(1)
    t.up()

def goCoords(coords):
    t.fd(coords[0])
    if coords[1] < 0:
        t.rt(90)
        t.fd(coords[1])
        t.down()
        t.color('red')
        t.circle(1)
        t.up()
        print(coords)
    else:
        t.lt(90)
        t.fd(coords[1])
        t.down()
        t.color('red')
        t.circle(1)
        t.up()
        print(coords)

drawCircle(100)

goCoords(genCoords())
#print(genCoords())
