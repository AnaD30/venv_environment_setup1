# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def main_menu():
        print("Welcome to the GAMEROOM!")
        print("\n--- Quiz Game Menu ---")

        print("1. Start Quiz 1")

        print("2. Start Quiz 2")

        print("3. Exit")

        choice = input("Enter your choice: ")


        if choice == '1':

            print("\n--- Starting Quiz 1 ---")

            #correct_guesses = quiz_game(questions_one, options_quiz_one)

           #display_score(correct_guesses, len(questions_one))

        elif choice == '2':

            print("\n--- Starting Quiz 2 ---")

            #correct_guesses = quiz_game(questions_two, options_quiz_two)

           # display_score(correct_guesses, len(questions_two))

        elif choice == '3':

            print("Thank you for playing! Goodbye!")
            exit()
        else:

            print("Invalid choice. Please try again.")
            

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the chemical symbol for Potassium?",
        "options": ["P", "Po", "K", "Li"],
        "correct_answer": "K"
    },
    {
        "question": "What year was Abraham Lincoln born?",
        "options": ["1909", "1811", "1809", "1776"],
        "correct_answer": "1809"
    },
    {
        "question": "What is the geographical name for a rainforest?",
        "options": ["Taiga", "Badlands", "Selvas", "Hardpan"],
        "correct_answer": "Selvas"
    }
]

def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
        
def get_user_answer():
    while True:
        try:
            choice = int(input("Enter your answer (1-4): "))
            if 1 <= choice <= 4:
                return choice - 1
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

main_menu()
