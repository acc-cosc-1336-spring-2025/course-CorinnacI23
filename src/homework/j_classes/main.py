from class_a import Die

def main():
    die = Die()
    while True:
        user_input = input("Roll the die? (y/n): ").lower()
        if user_input == 'y':
            die.roll()
            print(die)
        elif user_input == 'n':
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()

