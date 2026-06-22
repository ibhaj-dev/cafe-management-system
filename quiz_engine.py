# quiz_engine.py

def run_quiz(questions, options, answers):
    score = 0
    guesses = []

    for q_num, question in enumerate(questions):
        print("\n----------------------")
        print(question)

        for option in options[q_num]:
            print(option)

        guess = input("Enter (A/B/C/D): ").upper()
        guesses.append(guess)

        if guess == answers[q_num]:
            print("✔ Correct!")
            score += 1
        else:
            print("✖ Wrong! Correct answer:", answers[q_num])

    print("\n====== RESULTS ======")
    print("Correct Answers :", answers)
    print("Your Answers    :", guesses)

    percentage = int(score / len(questions) * 100)
    print(f"\nFinal Score: {percentage}%")

    if percentage == 100:
        print("🔥 Perfect Score!")
    elif percentage >= 70:
        print("👍 Good job!")
    else:
        print("💪 Keep practicing!")