import sys

dna_sequence = sys.argv[1]

dna_sequence_split = dna_sequence.split('X')
dna_sequence_split.sort()

print("fixed seq: ",dna_sequence_split)
