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
        "What is the capital of France?": {
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        "What is 2 + 2?": {
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        "What is the largest ocean on Earth?": {
            "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
            "answer": "D"
        },
        "What is the currency of Japan?": {
            "options": ["A) Dollar", "B) Euro", "C) Yen", "D) Won"],
            "answer": "C"
        },
        "What planet is known as the Red Planet?": {
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
    }
    score = 0
    for question, data in questions.items():
        print(question)
        for option in data["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {data['answer']}")
    return score

def quiz_game_two():
    questions = {
        "What is the capital of Japan?": {
            "options": ["A) Tokyo", "B) Seoul", "C) Beijing", "D) Bangkok"],
            "answer": "A"
        },
        "What is 5 * 6?": {
            "options": ["A) 28", "B) 30", "C) 32", "D) 34"],
            "answer": "B"
        },
        "What is the smallest planet in our solar system?": {
            "options": ["A) Mars", "B) Venus", "C) Mercury", "D) Earth"],
            "answer": "C"
        },
        "What is the chemical symbol for water?": {
            "options": ["A) O2", "B) CO2", "C) H2O", "D) H2"],
            "answer": "C"
        },
        "Who wrote 'Romeo and Juliet'?": {
            "options": ["A) Dickens", "B) Shakespeare", "C) Austen", "D) Twain"],
            "answer": "B"
        },
    }
    score = 0
    for question, data in questions.items():
        print(question)
        for option in data["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {data['answer']}")
    return score

def main():
    scoreboard = {"Game One": 0, "Game Two": 0}
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            score = quiz_game_one()
            scoreboard["Game One"] += score
            print(f"Total score in Quiz Game One: {scoreboard['Game One']}")
        
        elif choice == '2':
            score = quiz_game_two()
            scoreboard["Game Two"] += score
            print(f"Total score in Quiz Game Two: {scoreboard['Game Two']}")
        
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")
            continue
        
        # Provide feedback based on the score
        total_questions = 5  # Each quiz has 5 questions
        if score >= total_questions:
            print("Well done!")
        else:
            print("Better luck next time!")
        
        # Ask if the user wants to continue or exit
        continue_choice = input("Do you want to continue playing? (y/n): ")
        if continue_choice