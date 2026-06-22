# main.py

from quiz_engine import run_quiz
from quiz_data import (
    easy_questions, easy_options, easy_answers,
    medium_questions, medium_options, medium_answers,
    hard_questions, hard_options, hard_answers
)

print("WELCOME TO PYTHON QUIZ GAME 🎮")
print("----------------------")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Choose level (1/2/3): ")

if choice == "1":
    run_quiz(easy_questions, easy_options, easy_answers)

elif choice == "2":
    run_quiz(medium_questions, medium_options, medium_answers)

elif choice == "3":
    run_quiz(hard_questions, hard_options, hard_answers)
else:
    print("Invalid choice")