# main.py

from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers

def main():
    while True:
        print("\nHomework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            while True:
                num = input("Enter a number for factorial (1-9): ")
                try:
                    num = int(num)
                    if 1 <= num <= 9:
                        result = get_factorial(num)
                        print(f"The factorial of {num} is {result}")
                        break
                    else:
                        print("Please enter a number between 1 and 9.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        
        elif choice == '2':
            while True:
                num = input("Enter a number to sum odd numbers (1-99): ")
                try:
                    num = int(num)
                    if 1 <= num <= 99:
                        result = sum_odd_numbers(num)
                        print(f"The sum of odd numbers up to {num} is {result}")
                        break
                    else:
                        print("Please enter a number between 1 and 99.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        elif choice == '3':
            exit_choice = input("Do you want to exit? (y/n): ").lower()
            if exit_choice == 'y':
                print("Exiting the program...")
                break
            elif exit_choice == 'n':
                continue
            else:
                print("Invalid choice. Please choose 'y' to exit or 'n' to continue.")
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

