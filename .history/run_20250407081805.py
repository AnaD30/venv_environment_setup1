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
            "options": ["a)Osaka", "b)Nara", "c)Tokyo", "d)Sapporor"],
            "answer": "c"
        }
    ]

