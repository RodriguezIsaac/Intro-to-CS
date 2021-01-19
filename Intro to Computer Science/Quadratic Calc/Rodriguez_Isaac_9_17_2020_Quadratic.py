a = float(input("Choose a value for a."))
b = float(input("Choose a value for b."))
c = float(input("Choose a value for c."))
#Quadratic Formula Process
y = ((b ** 2 - 4 * a * c) ** 0.5)
x = (-b + y)
z = (-b - y)

try:
    f = round((x / (2 * a)), 2)
    g = round((z / (2 * a)), 2)
except TypeError: #Handling TypeError for Imaginary Answers
    print("Answer is Imaginary")
else: #Allowing Real Answers to go through
    print("x =", f)
    print("x =", g)