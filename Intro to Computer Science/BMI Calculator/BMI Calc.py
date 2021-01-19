height = float(input("What is your height in inches?"))
weight = float(input("What is your weight in pounds?"))

BMI = (703 * weight / height ** 2)
BMI = round(BMI,2)

if BMI <= 18.5:
    print("Your BMI is: ", BMI, "UnderWeight")
elif BMI > 18.5 and BMI <25:
    print("Your BMI is: ", BMI, "NormalWeight")
elif BMI >25 and BMI <30:
    print("Your BMI is: ", BMI, "OverWeight")
elif BMI >30:
    print("Your BMI is: ", BMI, "Obese")