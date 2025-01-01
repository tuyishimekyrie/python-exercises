import random


stat = True
while stat:
 inputs = input("Roll the dice (Y/N): ")
 value = inputs.lower()
 if value == "y":
    print(f"({ random.randint(1,6)}, {random.randint(1,6)})")
 elif value == "n":
    print("Thanks for playing!")
    stat = False
 else:
    print("Invalid choice!")
