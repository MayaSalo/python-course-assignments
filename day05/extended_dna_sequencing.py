dna_sequence = input("Please type in a sequence: ")

bases = ["A","T","C","G"]

new_seq = []
segment = ""
for char in dna_sequence:
  if char in bases:
    segment += char
  else:
    if segment:
      new_seq.append(segment)
      segment = ""

if segment:
  new_seq.append(segment)
  
new_seq.sort(key=len)

print("fixed seq: ",new_seq)

