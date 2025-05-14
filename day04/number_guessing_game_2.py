import random

random_number = random.randint(1, 20)

while True:
  user_input = input("Guess a whole number between 1 to 20, or x to exit: ")
  
  if user_input == 'x':
    print("Bye Bye :( ")
    exit()

  guess = int(user_input)
  
  if guess == random_number:
    print("CORRECT! you guessed the number!")
    break
  
  if guess > random_number:
    print("The number is smaller than your guess")
  else:
    print("The number is bigger than your guess")

