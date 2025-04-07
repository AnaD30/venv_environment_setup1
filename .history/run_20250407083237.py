# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def display_menu():
    print("Welcome to the Quiz Game!")
    print("1.Quiz Game 1")
    print("2.Quiz Game 2")
    print("3.Exit")
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
            
        
