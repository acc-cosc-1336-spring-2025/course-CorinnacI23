def main():
    # Get user input
    kilometers = int(input("Enter the number of kilometers: "))
    minutes = int(input("Enter the number of minutes: "))
    
    # Call the get_miles_per_hour function
    result = get_miles_per_hour(kilometers, minutes)
    
    # Display the result
    print(f"Speed: {result} miles per hour")

if __name__ == "__main__":
    main()
