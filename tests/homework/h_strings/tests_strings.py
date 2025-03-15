import unittest
from src.homework.h_strings.value_return import get_hamming_distance
from src.homework.h_strings.value_return import get_dna_complement

class Test_Config(unittest.TestCase):
    
    def test_get_hamming_distance(self):
        # Test case for Hamming distance function
        dna1 = "GAGCCTACTAACGGGAT"
        dna2 = "CATCGTAATGACGGCCT"
        self.assertEqual(get_hamming_distance(dna1, dna2), 7)
    
    def test_get_dna_complement(self):
        # Test case for DNA complement function
        dna = "AAAACCCGGT"
        self.assertEqual(get_dna_complement(dna), "ACCGGGTTTT")

if __name__ == '__main__':
    unittest.main()

   
            



