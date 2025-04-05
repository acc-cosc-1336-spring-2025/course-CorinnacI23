def get_p_distance(list1, list2):
    # Ensure both lists are of the same length
    if len(list1) != len(list2):
        raise ValueError("DNA strings must be of the same length.")
    
    # Count the number of differing symbols
    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    
    # Return the proportion of differing positions (p-distance)
    return differences / len(list1)

def get_p_distance_matrix(dna_sequences):
    n = len(dna_sequences)
    p_distance_matrix = []

    # Calculate the p-distance between all pairs of DNA sequences
    for i in range(n):
        row = []
        for j in range(n):
            # Calculate p-distance between sequence i and j
            p_distance = get_p_distance(dna_sequences[i], dna_sequences[j])
            row.append(round(p_distance, 5))  # Round to 5 decimal places
        p_distance_matrix.append(row)
    
    return p_distance_matrix