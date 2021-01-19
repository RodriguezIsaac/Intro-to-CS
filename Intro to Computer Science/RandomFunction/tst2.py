def increase(x) :
    xy = len(x)

    x[xy - 1] += 1
    carry = x[xy - 1] / 10
    x[xy - 1] = x[xy - 1] % 10

    for i in range(xy - 2, -1, -1) :
        if (carry == 1) :
            x[i] += 1
            carry = x[i] / 10
            x[i] = x[i] % 10


    if (carry == 1) :
        x.insert(0, 1)




vect = [9, 2, 3, 4]

increase(vect)

for i in range(0, len(vect)) :
    print(vect[i], end=" ")
