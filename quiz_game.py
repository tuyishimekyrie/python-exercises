game = [
    {
        "id":1,
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "A"
    },
    {
        "id":2,
        "question": "What is the capital of Germany?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "B"
    },
    {
        "id":3,
        "question": "What is the capital of Spain?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "D"
    },
    {
        "id":4,
        "question": "What is the capital of UK?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "C"
    }
]

total_score = 0

for index,question in enumerate(game):
    print(f"Question {question["id"]}: {question["question"]}")
    for index,option in enumerate(question["options"]):
     print(f"{option}")
    question_answer = input("Your answer:").upper()
    if question_answer == question["answer"]:
        print("Correct")
        total_score += 1
    else:
        print("Incorrect")
print(f"Your total score is {total_score}")
