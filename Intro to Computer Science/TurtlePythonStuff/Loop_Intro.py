#string look like this. they use parentheses
'''
string1 = ("rock, paper, scissors")
print (string1)
'''

#Lists use brackets. Computer start counting at 0
'''
list1 = ["rock", "paper", "scissors", "fire", "ice", "tanks"]
#print (list1) #(list1 [2]) prints what ever is listed in slot 2. If number is negative it starts from the end
for ducks in list1:
    #print("i like " + ducks)
    if ducks == "ice":
        continue #skips variable (ice) & continues
    print("i like " + ducks)
        #break #stops lopping from continuing after certain variable (ice)
'''

import turtle as t

t.speed(10)

def square ():

    for i in range(4): #range repeats commands a set number of times
        t.fd(200)
        t.rt(90)

def shape():
    for j in range(200):
        square()
        t.rt(2)

shape()

t.done()