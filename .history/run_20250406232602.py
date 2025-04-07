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
            
 def quiz_game_1():

    print("Welcome to Quiz Game 1!")

    score = 0

    questions = [

        {

            "question": "What is the capital of France?",

            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],

            "answer": "A"

        },

        {

            "question": "What is 2 + 2?",

            "options": ["A. 3", "B. 4", "C. 5", "D. 6"],

            "answer": "B"

        },

        {

            "question": "What is the largest planet in our solar system?",

            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],

            "answer": "C"

        }

    ]

    

    for q in questions:

        print(q["question"])

        for option in q["options"]:

            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:

            print("Correct!")

            score += 1

        else:

            print(f"Wrong! The correct answer is {q['answer']}.")

        print()  # Print a newline for better readability

    

    print(f"Your final score in Quiz Game 1: {score}/{len(questions)}")

    print()
           
main_menu()
quiz_game_1                  