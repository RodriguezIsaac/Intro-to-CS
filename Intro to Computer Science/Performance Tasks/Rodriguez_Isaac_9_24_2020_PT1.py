'''

RUBRIC
Getting user input correctly (5)
Correctly calculate water bill for 25,000 gallons or under (10)
Correctly calculate water bill for 50,000 gallons or under (10)
Correctly calculate water bill for over 50,000 gallons (10)
Display output clearly (10)
Commented code. (5)

Your local water company has hired you to write a program to process their customer billing. Below is the rate they charge their customers for water usage:

First 25,000 gallons cost $2.35 per 1000 gallons
Over 25,000 and up to 50,000 gallons cost $6.60 per 1000 gallons
Over 50,000 gallons is $8.84 per 1000 gallons
For example, if a customer uses 60,000 gallons (25000 + 25000 + 10000 = 60000 gallons), his/her water bill would be:
25000 * 2.35/1000 + 25000 * 6.60/1000 + 10000 * 8.84/1000
= 58.75 + 165 + 88.4
= $312.15
Write a program that prompts for the number of gallons of water usage, calculates the total bill, and display the total water bill for that customer in sentence form:
Total water bill is:
When finished, please copy and paste your code into a direct message to me on Rocket Chat. please surround your code with 3 backticks before the code and 3 backticks after the code. If your code shows up in a box (as opposed to just plain text) you did it right. ``` ```
'''

#Prompts User for amount of water gallons
Gallons = float(input("Welcome to your local water company. How many gallons of water do you have? "))

if Gallons <= 25000: #Does Equation below if gallon amount is below or equal to 25000
    print("Your total water bill is $", Gallons * 2.35/1000)
elif Gallons > 25000 <= 50000: #Does Equation below if gallon amount is inbetween 50000 or is 50000
    print("Your total water bill is $", 25000 * 2.35/1000 + (Gallons - 25000) * 6.60/1000)
elif Gallons > 50000: #Does Equations below if gallon amount is higher than 50000
    print("Your total water bill is $", 25000 * 2.35/1000 + 25000 * 6.60/1000 + (Gallons - 50000) * 8.84/1000)