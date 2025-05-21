import sys

bases = ["A","C","T","G"]

dna_sequence = sys.argv[1]

dna_sequence_split = dna_sequence.split('X')
print("splited seq: ",dna_sequence_split)

print("sorted seq: ",dna_sequence_split.sort())

