tasks = []
def display_input():
    print("1. view tasks")
    print("2. add task")
    print("3. delete task")
    print("4. exit")

def get_user_input():
    choice = input("Enter your choice: ")
    choice_list = ("1", "2", "3", "4")
    while True:
        if choice in choice_list:
         return choice
        else:
         print("Invalid input. Please enter a number.")
         return


def view_task():
    for task in tasks:
        print(task["task"])

def add_task():
    task = input("Enter the task ")
    tasks.append({"id": len(tasks) + 1, "task":task})

     
        
def main():
    display_input()
    while True:
     num = get_user_input()
     if num == "1":
      view_task()
      continue
     elif num == "2":
        add_task()
        continue
     elif num == "3":
      return
     elif num == "4":
      exit()
     else:
         get_user_input()

if __name__ == "__main__":
 main()