# quiz_data.py

easy_questions = (
    "What is the correct file extension for Python files?",
    "Which symbol is used for comments in Python?"
)

easy_options = (
    ("A. .pyth", "B. .pt", "C. .py", "D. .pyt"),
    ("A. //", "B. #", "C. :", "D. **")
)

easy_answers = ("C", "B")


medium_questions = (
    "Which of the following is immutable?",
    "Which function is used to get user input?"
)

medium_options = (
    ("A. list", "B. dictionary", "C. set", "D. tuple"),
    ("A. get()", "B. scan()", "C. input()", "D. read()")
)

medium_answers = ("D", "C")


hard_questions = (
    """What is the output?
a = [1, 2, 3]
b = a
b.append(4)
print(a)""",

    """What will happen here?
print(2 ** 3 ** 2)"""
)

hard_options = (
    ("A. [1, 2, 3]", "B. [4]", "C. [1, 2, 3, 4]", "D. Error"),
    ("A. 64", "B. 512", "C. 36", "D. 256")
)

hard_answers = ("C", "B")