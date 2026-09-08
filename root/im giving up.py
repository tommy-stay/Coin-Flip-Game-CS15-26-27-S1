import random

value = random.randint(1, 10)

choices = random.choice(["left", "right"])

choices = ["left", "right"]
choices = random.choice(choices)

guess = input("What is your guess?")
answer = input("Would you like to play again?")

guess = guess.lower()
answer = answer.lower()

while guess != value:
    guess = guess.lower()
    if guess == "left":
        print("Correct!")
        print("Would you like to play again?")
        if answer == "yes":
            print("What is your guess?")
            if answer == "no":
                print("Okay then! Goodbye!")

        guess = guess.lower()
    if guess == "right":
            print("Wrong!")
