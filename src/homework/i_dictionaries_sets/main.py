from dictionary import get_p_distance_matrix

def main():
    while True:
        # Display the menu
        print("1- Get p-distance matrix")
        print("2- Exit")
        
        # Get the user's choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt the user to enter the DNA sequences
            print("Please enter the DNA sequences (separated by commas):")
            input_sequences = input().split(',')
            dna_sequences = [list(seq.strip()) for seq in input_sequences]
            
            # Get the p-distance matrix
            p_distance_matrix = get_p_distance_matrix(dna_sequences)
            
            # Display the matrix
            for row in p_distance_matrix:
                print(' '.join(f"{x:.5f}" for x in row))
        
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()


