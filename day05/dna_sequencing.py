import sys

dna_sequence = sys.argv[1]

dna_sequence_split = dna_sequence.split('X')

dna_sequence_split = [segment for segment in dna_sequence_split if segment]

dna_sequence_split.sort(key=len)

print("fixed seq: ",dna_sequence_split)
