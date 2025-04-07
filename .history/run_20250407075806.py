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
        "question": "What is the capital of China ?",
        "options": ["Beijing", "Singapur", "Xian", "Shanghai"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the capital from ?",
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
            
            
def run_quiz():
    score = 0
    total_questions = len(questions)
    
    random.shuffle(questions)
    
    for question in questions:
        display_question(question)
        user_choice = get_user_answer()
        
        if question["options"][user_choice] == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {question['correct_answer']}")
        
        print()  # Add a blank line for readability
    
    print(f"Quiz complete! You scored {score} out of {total_questions}.")
    percentage = (score / total_questions) * 100
    print(f"Your score: {percentage:.2f}%")
    
    
main_menu()
get_user_answer()
run_quiz()
