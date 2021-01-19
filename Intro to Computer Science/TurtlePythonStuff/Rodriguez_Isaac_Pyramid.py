import turtle as t

w = float(input("Please provide a value for the width. "))
l = float(input("Please provide a value for the length. "))
h = float(input("Please provide a value for the height. "))

t.penup()

def pyramid():
        t.goto(0,100)
        t.pendown()
        t.pensize(3)
        t.goto(35,-50)
        t.goto(-67,-23)
        t.goto(0,100)
        t.goto(94, -14)
        t.goto(35, -50)
        t.penup()
        t.goto(0,100)
        t.pendown()
        t.goto(5,0)
        t.goto(-70,-20)
        t.goto(5,0)
        t.goto(94,-14)

pyramid()

t.penup()

t.setpos(70, -45)
t.write(('Width =',w), font=("Times New Roman", 12, "bold"))

t.setpos(-93, -65)
t.write(('Length =',l), font=("Times New Roman", 12, "bold"))

t.setpos(0, 110)
t.write(('Height =',h), font=("Times New Roman", 12, "bold"))

V = round(((w * l * h)/3), 2)

t.setpos(0, -100)
t.write(('Volume =',V), font=("Times New Roman", 12, "bold"))

t.done()