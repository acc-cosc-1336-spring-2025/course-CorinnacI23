## src/homework/h_strings/main.py
from value_return import get_hamming_distance, get_dna_complement

def main():
    while True:
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            dna1 = input("Enter the first DNA string: ")
            dna2 = input("Enter the second DNA string: ")
            print(f"Hamming Distance: {get_hamming_distance(dna1, dna2)}")
        
        elif choice == '2':
            dna = input("Enter the DNA string: ")
            print(f"DNA Complement: {get_dna_complement(dna)}")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
