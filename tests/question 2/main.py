# main.py

def main():
    while True:
        # Prompt the user for input
        user_input = input("Enter a number to check if it's prime (or 'quit' to exit): ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("Exiting the program.")
            break
        
        # Ensure the input is a valid number
        try:
            number = int(user_input)
            # Check if the number is prime and display the result
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Please enter a valid integer or 'quit' to exit.")
    
if __name__ == "__main__":
    main()
