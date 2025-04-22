import random

random_number = random.randint(1, 20)

guess = int(input("Guess a whole number between 1 to 20: "))

if guess > random_number:
    print("The number is smaller than your guess")
elif guess < random_number:
    print("The number is bigger than your guess")
else:
    print("CORRECT! you guessed the number!")
