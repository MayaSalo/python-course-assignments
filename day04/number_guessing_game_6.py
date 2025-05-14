import random

random_number = random.randint(1, 20)

debug_mode = False
move_mode = False
new = False

while True:

  if new:
    random_number = random.randint(1, 20)

  if debug_mode:
    print("Debug - The number is: ",random_number)

  if move_mode:
    addition = random.randint(-2, 2)
    random_number = random_number+addition
    
  user_input = input("Enter your guess [x for exit, s for help, d for debug, m for move, n for new]: ")
  
  if user_input == 'x':
    print("Bye Bye :( ")
    exit()
  elif user_input == 's':
    print("The number is: ",random_number)
    continue
  elif user_input == 'd':
    debug_mode = not debug_mode
    continue  
  elif user_input == 'm':
    move_mode = not move_mode
    continue    
  elif user_input == 'n':
    print("ready for a new game?")
    new = not new
    continue     

  guess = int(user_input)
  
  if guess == random_number:
    print("CORRECT! you guessed the number!")
    print("ready for a new game?")
    new = not new
    continue
  
  if guess > random_number:
    print("The number is smaller than your guess")
  else:
    print("The number is bigger than your guess")


