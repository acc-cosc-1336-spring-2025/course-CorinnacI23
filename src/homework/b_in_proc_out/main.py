## src/homework/c_decisions/main.py
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

def main():
    # Prompt user for input
    options = float(input("Enter the number of options: "))  # Convert to float
    total = float(input("Enter the total: "))  # Convert to float
    
    # Calculate the ratio
    result = get_options_ratio(options, total)
    
    # Get the rating
    rating = get_faculty_rating(result)
    
    # Display the result
    print(f"The faculty rating is: {rating}")

if __name__ == '__main__':
    main()
