# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys


def display_menu():
    print("\n=== Quiz Game Menu ===")
    print("1. Play Quiz Game One")
    print("2. Play Quiz Game Two")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def quiz_game_one():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest ocean on Earth?": "Pacific",
        "What is the currency of Japan?": "Yen",
        "What planet is known as the Red Planet?": "Mars",
    }
    score = 0
    for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
    print(f"Your final score in Quiz Game One: {score}/{len(questions)}")
    return score

def quiz_game_two():
    questions = {
        "What is the capital of Japan?": "Tokyo",
        "What is 5 * 6?": "30",
        "What is the smallest planet in our solar system?": "Mercury",
        "What is the chemical symbol for water?": "H2O",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    }
    score = 0
    for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
    print(f"Your final score in Quiz Game Two: {score}/{len(questions)}")
    return score

def main():
    scoreboard = {"Game One": 0, "Game Two": 0}
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            score = quiz_game_one()
            scoreboard["Game One"] += score
            play_again = input("Do you want to play Quiz Game One again? (y/n): ")
            if play_again.lower() != 'y':
                print(f"Total score in Quiz Game One: {scoreboard['Game One']}")
        
        elif choice == '2':
            score = quiz_game_two()
            scoreboard["Game Two"] += score
            play_again = input("Do you want to play Quiz Game Two again? (y/n): ")
            if play_again.lower() != 'y':
                print(f"Total score in Quiz Game Two: {scoreboard['Game Two']}")
        
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()