#I'm Learning

print("Hello World!")

"""
anything between the opening and closing quotes will be ignored/commented out
"""

print("Mr. Berta's Class is Awesome!")

print (5 + 4)
print ("5 + 4")

#Doing Math Equations with Code
'''
print (5 + 6 * 3)
print (6 * 3 + 5)
print ((5 + 6) * 3) #The 5 + 6 will be evalutated before the times 3
'''

#Declaring Variables
'''
firstname = ("Isaac")
lastname = ("Rodriguez")

print (firstname + lastname) #You can combine what is to be printed

firstname = ("Isaac")
print (firstname) #Prints the firstname above it (most recent)
print (lastname)

space = ("Newton")
print (firstname + space + lastname)
'''

#Combining string data with numeric data
'''
problem = ("7 * 3")
solution = (7 * 3)

print (problem + " = " + str(solution))

number1 = int (7) #results in 7
number2 = float (7) #results in 7.0

print (number1)
print (number2)
'''

#syntax errors prevent code from even running
#runtime errors allows code to run until it encounters an error

#Getting input from user
firstname = input("What is your first name?")
lastname = input("What is your last name?")

print("You entered: " + firstname + " " + lastname)


#Conditional Statements
pooltemp = 75

if pooltemp > 85:
    print ("This is perfect pool temperature")
elif 75 <= pooltemp <= 85:
    print("We'll go in, but we might no stay long.")
else:
    print("heck with that, it's too cold")

#Error Handling   
a = float(input("Please enter a number"))
b = float(input("Please enter a number to divide by"))
try:
    print(a / b)
except ZeroDivisionError:
    print("You can't divide by zero")


def sayhi ():
    print("Hi")
    print("How are you today?")
    print("Have a nice day")

