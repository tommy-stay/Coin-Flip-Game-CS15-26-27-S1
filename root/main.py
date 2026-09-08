import random

strikes = 0

while strikes < 3:
    coin = random.choice(["Heads", "Tails"])


    while True:
        guess = input("Enter your guess (Heads or Tails): ")
        if guess in ["Heads", "Tails"]:
            break
        print("Invalid input. Please enter 'Heads' or 'Tails'.")


    if guess == coin:
        strikes = 0
        print(f"Correct! The coin landed on {coin}. Strikes: {strikes}/3")
        print("Congratulations!🥳🥳🥳")
    else:
        strikes += 1
        print(f"Incorrect! The coin landed on {coin}. Strikes: {strikes}/3")

print("\nGame Over! You reached 3 strikes in a row.")