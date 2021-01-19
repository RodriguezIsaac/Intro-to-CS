import turtle as t
import random

t.hideturtle()
t.colormode(255)
t.speed('fastest')
t.pensize(6)

def color():
    global r, g, b
    r = random.randrange(0, 255, 10)
    g = random.randrange(0, 255, 10)
    b = random.randrange(0, 255, 10)

def Square():
    for i in range(4):
        color()
        t.pencolor(r, g, b)
        t.fd(100)
        t.lt(90)

def Shape():
    t.clear()
    for s in range(24):
        Square()
        t.lt(15)

def Spiral():
    t.clear()
    for s in range(61):
        color()
        t.pencolor(r, g, b)
        t.fd(100 + s)
        t.lt(60)

def Star():
    t.clear()
    for n in range(200):
        color()
        t.pencolor(r, g, b)
        t.fd(200 + n)
        t.rt(144)

def Twinkle_Star():
    for m in range(8):
        color()
        t.pencolor(r, g, b)
        t.rt(175)
        t.fd(150)
        t.rt(50)
        t.fd(150)

def Shape1():
    t.clear()
    for w in range(7):
        Twinkle_Star()
        t.lt(100)

options = [Shape, Spiral, Star, Shape1]

def program():
    for p in range(4):
        R = random.choice(options)
        R()
        options.remove(R)

program()

t.done()