import random

random_number = random.randint(1, 20)

guess = int(input("Guess a whole number between 1 to 20: "))

while guess != random_number:
  if guess > random_number:
    print("The number is smaller than your guess")
    guess = int(input("Guess a different whole number between 1 to 20: "))
  elif guess < random_number:
    print("The number is bigger than your guess")
    guess = int(input("Guess a different whole number between 1 to 20: "))

print("CORRECT! you guessed the number!")
