#!/Users/Amarsing/anaconda3/bin/python
# Given a string, count the number of times each word appears

dna = "TGGATGCGGTGAATAGCAGTACACTCGTGCTTCTCGCTCATCTGACTATATCTCACTGGAAAGTGCTTGGGTTTAAGGCGGAGTATGGGCTCAAGCCCTAGATGCCCCAATCTAGTGAACGACTACAGTGCCAGTGGTATACCGGCTAACCCATCTCAAGAATGCCTACCGGTGGGCAGCCTAAGGGGAGTCGCCGGTTAAACTCGTGCACTGTCGCTGACTTCACGGGACTGCAAGCATTGCACATTTAAACGCTACCCGAAAGCTTTACTGTCTAGAGTAGTTAGTATAGCAGCTTGCGGGTCAGCATCGCCGTATGAATATAATAGGCCCCATGCGCGAACGGGGGCTAGACGGCACTAACTAAATATAGCATTAGCTAGAGCTATGCATGGTAAGAGAACAGACAAGAGGGTAAGTTCTGTCCTATCTTTAGTTTTGCCACCCTTTTCCCCTCATCTTGGCTCGCGGTTCCAGCCAGTATATCCGCATCTGTCCTCTCGTTGACCTCGAGGTAGCTGCCTTATAGACTCATAAGGGTCTACATCTTGGATGTTGGGGAATCTGTTATCAAACGAGCCGTACATTACCTAGGATGATTAGTAGGATAGTTGCTGAATGACTCTGGGGGCGAAGGAATTTTACGAAATACCCAAGAGAGGCTCGCGAGAATCGGCGGCACAAGGGACAGTTTCTAGCACCGCTTTTCGGAGCATGGTAATTGGTACCACGGATAACGCTGGTCGGCTCAGCCTCAAGCCCGCTATCCGCAGTAGTGATAGCTTTATACCTCAGGGAACATGTGCTGCTTTTCGAGAGAAAGCAA"
dna = dna.upper()

# Create a list of all the words in the string

dna_dict = {"A":0, "C":0, "G":0, "T":0}

# Add each word to a dictionary and count the number of times it occurs
for base in dna:
    if base in dna_dict:
        dna_dict[base] += 1

print(str(dna_dict['A']) + ' ' + str(dna_dict['C']) + ' ' + str(dna_dict['G']) + ' ' + str(dna_dict['T']))