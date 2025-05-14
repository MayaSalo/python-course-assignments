import random

random_number = random.randint(1, 20)

debug_mode = False

while True:

  if debug_mode:
    print("Debug - The number is: ",random_number)
    
  user_input = input("Enter your guess [x for exit, s for help, d for debug]: ")
  
  if user_input == 'x':
    print("Bye Bye :( ")
    exit()
  elif user_input == 's':
    print("The number is: ",random_number)
    continue
  elif user_input == 'd':
    debug_mode = not debug_mode
    continue    

  guess = int(user_input)
  
  if guess == random_number:
    print("CORRECT! you guessed the number!")
    break
  
  if guess > random_number:
    print("The number is smaller than your guess")
  else:
    print("The number is bigger than your guess")
