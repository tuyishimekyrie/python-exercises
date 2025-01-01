import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"

def continue_game():
    value = input("Do you want to continue (Y/N): ").lower()
    if value == "y":
        return True
    elif value == "n":
        print("Thanks for playing!")
        return False
    else:
        print("Invalid choice!")
        return continue_game()

def output(input_value, computer_value,target_value):
    if input_value == ROCK and computer_value[target_value] == ROCK:
            print("It's a tie!")
    elif input_value == ROCK and computer_value[target_value] == PAPER:
        print("You win!")
    elif input_value == ROCK and computer_value[target_value] == SCISSORS:
        print("You lose!")
    elif input_value == PAPER and computer_value[target_value] == ROCK:
        print("You lose!")
    elif input_value == PAPER and computer_value[target_value] == PAPER:
        print("It's a tie!")
    else:
        print("Computer Win")
    value = continue_game()
    if value == False:
        exit()

def get_user_choice(computer_value,target_value,emojis):
    input_value = input("Rock, Paper or Scissors? (r/p/s): ").lower()
    if input_value == ROCK:
        print(f"You chose {input_value} is {emojis["r"]}")
        print(f"Computer chose {computer_value[target_value]} {emojis[input_value]}")
        output(input_value, computer_value,target_value)
    elif input_value == PAPER:
        print(f"You chose {input_value} is {emojis["p"]}")
        print(f"Computer chose {computer_value[target_value]} {emojis[input_value]}")
        output(input_value, computer_value,target_value)
    elif input_value == SCISSORS:
        print(f"You chose {input_value} is {emojis["s"]}")
        print(f"Computer chose {computer_value[target_value]} {emojis[input_value]}")
        output(input_value, computer_value,target_value)
    else:
        print(f"Invalid choice! {input_value}")

while True:

    emojis = {ROCK:"🪨", PAPER:"📜", SCISSORS:"✂️"}
    target_value = random.randint(0,2)
    computer_value = tuple(emojis.keys())

    get_user_choice(computer_value,target_value,emojis)
    
    
   
