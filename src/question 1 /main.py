def get_miles_per_hour(kilometers, minutes):
    # Check for invalid negative arguments
    if kilometers < 0 or minutes < 0:
        return 'Invalid arguments'
    
    # Conversion factor from kilometers to miles
    conversion_ratio = 0.621371
    
    # Calculate miles per hour
    miles = kilometers * conversion_ratio
    miles_per_hour = miles / (minutes / 60)  # Convert minutes to hours
    
    return miles_per_hour


def is_prime(number):
    # Check if the number is less than or equal to 1 (not prime)
    if number <= 1:
        return False
    
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If divisible, it's not prime
    
    return True  # If no divisors found, it's prime


def main():
    # Loop for running both the prime number check and miles per hour calculation
    while True:
        # Ask the user what they want to do
        choice = input("Choose an option: (1) Check if a number is prime, (2) Calculate miles per hour, (3) Quit: ")
        
        if choice == '1':
            # Prime number check
            number = int(input("Enter a number to check if it's prime: "))
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        
        elif choice == '2':
            # Miles per hour calculation
            kilometers = int(input("Enter the number of kilometers: "))
            minutes = int(input("Enter the number of minutes: "))
            result = get_miles_per_hour(kilometers, minutes)
            print(f"Speed: {result} miles per hour")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

