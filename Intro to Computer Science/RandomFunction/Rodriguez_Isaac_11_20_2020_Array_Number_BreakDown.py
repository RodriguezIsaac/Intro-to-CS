Number = input("Provide a Positive Whole Number. ")

Digits = [int(d) for d in str(Number)]

print(f"The Digits of the Number you gave are: {Digits}")


def NewNum():
    NewDigit = Digits[-1] + 1
    Digits[-1] = NewDigit
    if len(Digits) > 1 and Digits[-1] == 10:
        for n in range(0, len(Digits) + 1):
            if not Digits[-n - 1] == 10:
                break
            Digits[-n - 1] = 0
            NewDigit2 = Digits[-n - 2] + 1
            Digits[-n - 2] = NewDigit2
            if Digits[0] == 10:
                Digits[0] = 0
                Digits.insert(0, 1)

NewNum()


print(f"The Last Digit of your Number plus 1 = {Digits}")