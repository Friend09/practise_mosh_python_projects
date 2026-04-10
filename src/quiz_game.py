# src/quiz_game.py

"""
Program to a quiz where the player answers multiple-choice questions.
The program should evaluate the player's answers and provide a score at the end.
"""

import sys
from termcolor import colored, cprint
import random

# question bank
def get_question_and_answers(number_of_questions: int) -> dict:
    questions = {
    1: {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome"],
        "answer": "a"
    },
    2: {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars"],
        "answer": "b"
    },
    3: {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2"],
        "answer": "c"
    },
    4: {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Pacific"],
        "answer": "c"
    }}

    return random.sample(list(questions.values()), number_of_questions)

if __name__ == "__main__":
    get_question_and_answers(2)
