Temperature = input("Choose a temperature unit between F, K, and C. ")
Degrees = float(input("Now choose a temperature. "))

try:
    F = round(float(((Degrees-32) * 5/9)), 2) #Formula for Fahrenheit to Celsius
    f = round(float(((Degrees - 32) * 5/9 + 273.15)), 2) #Formula for Fahrenheit to Kelvin

    K = round(float(((Degrees - 273.15) * 9/5 + 32)), 2) #Formula for Kelvin to Fahrenheit
    k = round(float(((Degrees - 273.15))), 2) #Formula for Kelvin to Celsius

    C = round(float(((Degrees * 9/5) + 32)), 2) #Formula for Celsius to Fahrenheit
    c = round(float(((Degrees + 273.15))), 2) #Formula for Celsius to Kelvin
except ZeroDivisionError:
    print("Can't divide by zero")

if Temperature == "F":
    print(Degrees, "degrees of Fahrenheit is equivalent to", F, "degrees Celsius and", f,"degrees Kelvin.")
elif Temperature == "K":
    print(Degrees, "degrees of Kelvin is equivalent to", k, "degrees Celsius and", K, "degrees Fahrenheit.")
elif Temperature == "C":
    print(Degrees, "degrees of Celsius is equivalent to", C, "degrees Fahrenheit and", c, "Kelvin.")
else:
    print("You have chosen a unit not displayed in the first question")