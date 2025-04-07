# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def menu():
    while True:
        print("\n--- Quiz Game Menu ---")

        print("1. Start Quiz 1")

        print("2. Start Quiz 2")

        print("3. Exit")

        choice = input("Enter your choice: ")


        if choice == '1':

            print("\n--- Starting Quiz 1 ---")

        elif choice == '2':

            print("\n--- Starting Quiz 2 ---")

        elif choice == '3':

            print("Thank you for playing! Goodbye!")

            break

        else:

            print("Invalid choice. Please try again.") 
            
    

    

menu()

