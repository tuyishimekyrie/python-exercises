import random

target = random.randint(1,100)

while True:
 try:
    input = int(input("Guess a number between 1 and 100: "))
    if input > target:
        print("The number is too high")
    elif input < target:
        print("The number is too low")
    else:
        print("Congratulations! You guessed the number!")   
        break
 except ValueError:
  print("Please enter a valid number")
