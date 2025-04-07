# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def main_menu():
        print("\nMain Menu")

        print("1. Play Number Guessing Game")

        print("2. Exit")
        

        choice = input("Choose an option (1-2): ")
        

        if choice == '1':

            while True:

                number_guessing_game()

                play_again = input("Do you want to play again? (yes/no): ").strip().lower()

                if play_again != 'yes':
                    break

        elif choice == '2':

            print("Thank you for playing! Goodbye!")

        else:

            print("Invalid choice. Please try again.")
main_menu()                  