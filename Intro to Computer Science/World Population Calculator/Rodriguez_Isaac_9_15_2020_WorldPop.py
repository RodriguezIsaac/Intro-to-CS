FutureYear = int(input("Choose a future year."))

t = (FutureYear - 2020)
P = 7800000000 #Current Population Size at the time of doing this assignment
e = 2.7182818284590452353602874713527 #Euler Number
rt= (0.0105 * t)

F = round((P * e ** rt), 0)


print("The estimated population of", FutureYear, "is", F,)