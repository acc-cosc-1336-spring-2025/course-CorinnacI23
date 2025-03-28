# src/homework/I_dictionaries_sets/main.py

from lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("Menu:")
        print("1. Show the list low/high values")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            numbers = []
            while True:
                try:
                    value = int(input("Enter a list value: "))
                    numbers.append(value)
                    
                    if len(numbers) >= 3:
                        more = input("Do you want to enter another value? (yes/no): ").strip().lower()
                        if more != 'yes':
                            break
                except ValueError:
                    print("Please enter a valid integer.")
            
            lowest_value = get_lowest_list_value(numbers)
            highest_value = get_highest_list_value(numbers)
            
            print(f"The lowest value is: {lowest_value}")
            print(f"The highest value is: {highest_value}")
        
        elif choice == '2':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


