pv = 35000 #Present Value for Car
r = 0.004167 #Monthly Interest Rate
n = 60 #Total Number of Months

#Interest Formula
p = float(round((r * pv) / (1 - (1 + r) ** -n), 2))

print("The purchase price for the Tesla Model 3 is", pv, "dollars.")
print("The annual interest rate for the loan is 5%.")
print("The loan is expected to be payed off in 5 years.")
print("The monthly payment amount for the Tesla Model 3 is", p, "dollars.")