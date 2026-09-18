questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Python", "B. Java", "C. C++", "D. HTML"],
        "answer": "A"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter Answer: ").upper()

    if user_answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")

print("\nFinal Score:", score, "/", len(questions))
