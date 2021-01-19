import random #Allows Randomization
import json
import urllib.request
import urllib.error


with open("WordList.txt", "r") as f: #Opens Stated File in read mode
    words = f.readlines() #Reads lines in the stated file

word = random.choice(words)[: -1] #Chooses a random word from the stated file up to the last line

try:
    #set url variable as openweathermap api query
    Knowledge = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    #opens the specifed url
    requestURL = urllib.request.urlopen(Knowledge)
    #read the information from the website and store as a variable
    data = requestURL.read()
    #encodes the data in UTF 8 format
    encoding = requestURL.info().get_content_charset('utf-8')
    #converts the data that is read to a json object
    Meaning = json.loads(data.decode(encoding))

    Definition = Meaning[0]["meanings"][0]["definitions"][0]["definition"]
    print(f"Definition: {Definition}\n")
except (IndexError, urllib.error.HTTPError):
    print("No Definition Found from API....Good Luck\n")

allowed_errors = 7
guesses = []

done = False #Game doesn't end quite yet

while not done: #While not done, play the game
    for letter in word:
        if letter.lower() in guesses: #Determines if the letter guessed is in the word
            print(letter, end = " ")
        else:
            print("_", end  = " ")
    print("")

    print(f"Guessed Letters: " + ", ".join(guesses))

    guess = input(f"Allowed Errors Left: {allowed_errors}, Next Guess: ")
    print("\n")
    guesses.append(guess.lower()) #Attaches guess to guesses
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0: #If maximum amount of errors is reached, break the loop (End the Code)
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses: #Continues the Loop when the a letter is guessed incorrectly
            done = False

try:
    if done:
        print(f"You found the word! It was {word}")
        print(f"Definition: {Definition}\n")
    else:
        print(f"Game Over! The word was {word}\n")
        print(f"Definition: {Definition}")
except NameError:
    print("")