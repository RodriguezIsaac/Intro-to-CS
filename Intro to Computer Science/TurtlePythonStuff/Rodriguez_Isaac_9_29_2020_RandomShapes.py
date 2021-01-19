#I got too intrigued to stop. Take Your Pick :D

#todo Weird Pokeball type thing. Maximize your window
'''
import turtle as t

t.speed('fastest')

t.pensize(3)
t.pencolor("purple")

t.setpos(-100, 25)

def shape():
    for j in range(8):
        t.fd(100)
        t.lt(45)
        t.fd(50)
        t.rt(66)
        t.rt(21)

def shape1():
    for k in range(38):
        shape()
        t.rt(50)
        t.fd(25)

shape1()

t.done()
'''

#todo Solid Circle Placement. Maximize your window
'''
import turtle as t

t.speed('fastest')

t.pensize(3)
t.pencolor("blue")

def shape():
    for k in range(30):
        t.rt(50)
        t.fd(25)
        t.lt(45)
        t.lt(18)
        t.fd(25)
        t.rt(80)
        t.fd(75)

def shape1():
    for l in range(7):
        shape()
        t.fd(10)
        t.lt(27)
        t.fd(30)
        t.rt(60)
        t.fd(50)
        t.lt(90)
        t.fd(90)

shape1()

t.done()
'''

#todo Clean Loop. Maximize your window
'''
import turtle as t

t.speed('fastest')

t.pensize(3)
t.pencolor("blue")

t.setpos(700, 0)

def shape():
    for k in range(15):
        t.rt(65)
        t.fd(26)
        t.lt(86)
        t.rt(21)
        t.rt(21)
        t.fd(64)

def shape1():
    for l in range(40):
        shape()
        t.lt(74)
        t.fd(81)
        t.rt(110)
        t.fd(178)

shape1()

t.done()
'''
