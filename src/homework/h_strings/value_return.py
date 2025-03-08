# src/homework/h_strings/value_return.pyh_strings

def get_hamming_distance(dna1, dna2):
    # Initialize the Hamming distance counter
    hamming_distance = 0
    
    # Loop through both strings and compare each character
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
            
    return hamming_distance
# src/homework/h_strings/value_return.py

def get_dna_complement(dna):
    complement = ''
    
    # Loop through the string in reverse order
    for i in range(len(dna) - 1, -1, -1):
        if dna[i] == 'A':
            complement += 'T'
        elif dna[i] == 'T':
            complement += 'A'
        elif dna[i] == 'C':
            complement += 'G'
        elif dna[i] == 'G':
            complement += 'C'
    
    return complement
