import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))


from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def menu():
    while True:
        print("\nHomework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                try:
                    num = int(input("Enter a number (1-9): "))
                    if 1 <= num < 10:
                        print(f"Factorial of {num} is {get_factorial(num)}")
                        break
                    else:
                        print("Number must be between 1 and 9.")
                except ValueError:
                    print("Please enter a valid integer.")

        elif choice == '2':
            while True:
                try:
                    num = int(input("Enter a number (1-99): "))
                    if 1 <= num < 100:
                        print(f"Sum of odd numbers up to {num} is {sum_odd_numbers(num)}")
                        break
                    else:
                        print("Number must be between 1 and 99.")
                except ValueError:
                    print("Please enter a valid integer.")

        elif choice == '3':
            confirm = input("Do you want to exit? (y/n): ").lower()
            if confirm == 'y':
                print("Exiting the program.")
                break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

menu()
