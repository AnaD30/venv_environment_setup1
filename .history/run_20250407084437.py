# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def display_menu():
    print("Welcome to the Quiz Game!")
    print("1.Quiz Game 1")
    print("2.Quiz Game 2")
    print("3.View Scoreboard")
    print("4.Exit")
    choice = input("Please select an option(1-3): ")
    return choice

def quiz_game_one():
    questions = [
        {
            "questions": "What is the capital of China?",
            "options": ["a)Beijing", "b)Shanghai", "c)Guangzhou", "d)Shenzhen"],
            "answer": "a"
        },
        {
            "questions": "What is the capital of Slovenia?",
            "options": ["a)Maribor", "b)Ljubljana", "c)Ptuj", "d)Celje"],
            "answer": "b"
        },
        {
            "questions": "What is the capital of Austria?",
            "options": ["a)Graz", "b)Salzburg", "c)Linz", "d)Wien"],
            "answer": "d"
        },
        {
            "questions": "What is the capital of Japan?",
            "options": ["a)Osaka", "b)Nara", "c)Tokyo", "d)Sapporo"],
            "answer": "c"
        }
    ]
    return run_quiz(questions)

def quiz_game_two():
     questions = [
        {
            "questions": "What is the capital of USA?",
            "options": ["a)Washington D.C.", "b)Texas", "c)New York", "d)Miami"],
            "answer": "a"
        },
        {
            "questions": "What is the capital of India?",
            "options": ["a)Mumbay", "b)New Delhi", "c)Calcuta", "d)Bunglalore"],
            "answer": "b"
        },
        {
            "questions": "What is the capital of Peru?",
            "options": ["a)Huaraz", "b)Huaraz", "c)Lima", "d)Cajamarca"],
            "answer": "c"
        },
        {
            "questions": "What is the capital of Canada?",
            "options": ["a)Toronto", "b)Vancouver", "c)Quebec city", "d)Ottawa"],
            "answer": "d"
        }
    ]
    return run_quiz(questions)

def run_quiz(questions):
    score = 0
    for q in questionss:
        print(q["questions"])
        for option in q["options"]:
            print(option)
        answer = input ("Your answer (a/b/c/d): ").lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"No,..!The correct answer is {q['answer']}.\n")
    return score 
        
def display_scoreboard(scores):
    print("Scoreboard:")
    for quiz_name, score in scores.items():
        print(f"{quiz_name} : {score}/3")
    print()
    
def main():
    choice = display_menu()
    if choice == "1":
        score = quiz_game_one()
        scores["Quiz Gamee One"] = score
        print(f"Your score for the Quiz Game One : {score} / {3} \n")
    elif choice == "2":
        score = quiz_game_two()
        scores["Quiz Gamee Two"] = score
        print(f"Your score for the Quiz Game Two : {score} / {3} \n")
    elif choice == "3":
        display_scoreboard(scores)
    elif choice == "4":
        print("Thank you for playing!")
        sys.exit() 
    else:
        print