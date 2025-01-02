from termcolor import cprint

OPTIONS = ["A", "B", "C", "D"]

game = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "A"
    },
    {
        "id": 2,
        "question": "What is the capital of Germany?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "B"
    },
    {
        "id": 3,
        "question": "What is the capital of Spain?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "D"
    },
    {
        "id": 4,
        "question": "What is the capital of the UK?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "C"
    }
]

def display_question(question):
    """Display a single question and its options."""
    print(f"\nQuestion {question['id']}: {question['question']}")
    for index, option in enumerate(question["options"], start=1):
        print(f"{OPTIONS[index - 1]}. {option}")

def get_user_answer():
    """Get and validate the user's answer."""
    while True:
        answer = input("Your answer: ").strip().upper()
        if answer in OPTIONS:
            return answer
        else:
            cprint("Invalid input. Please enter A, B, C, or D.", "yellow")

def ask_question(question):
    """Ask a question, get the answer, and return if the answer is correct."""
    display_question(question)
    user_answer = get_user_answer()
    if user_answer == question["answer"]:
        cprint("Correct!", "green")
        return True
    else:
        cprint("Incorrect!", "red")
        return False

def run_quiz(game):
    """Run the quiz and calculate the score."""
    total_score = 0
    for question in game:
        if ask_question(question):
            total_score += 1
    return total_score

def display_results(score, total_questions):
    """Display the final score."""
    print(f"\nYour total score is {score}/{total_questions}")
    cprint("Thanks for playing!", "cyan")

# Main program
if __name__ == "__main__":
    total_score = run_quiz(game)
    display_results(total_score, len(game))
