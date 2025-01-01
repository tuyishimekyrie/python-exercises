import random

while True:
 value = input("Roll the dice (Y/N): ").lower()

 if value == "y":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f"({ die1}, {die2})")
 elif value == "n":
    print("Thanks for playing!")
    break
 else:
    print("Invalid choice!")
