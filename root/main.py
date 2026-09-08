import random

value = random.randint(1, 10)

value = random.choice(["left", "right"])


choices = ["left", "right"]
value = random.choice(choices)

guess = input("What is your guess?")

guess = guess.lower()

while value != guess:
    guess = guess.lower()
    if guess == "left":
        print("Correct!")


    if guess == "right":
        print("Wrong!")
        value = input("What is your guess?")