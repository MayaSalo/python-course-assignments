import sys
import os

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} FILENAME")
    exit()

input_file = sys.argv[1]
output_file = 'report.txt'

digit_counts = {str(d): 0 for d in range(10)}

with open(input_file, 'r') as fh:
    contents = fh.read()
    for ch in contents:
        if ch.isdigit():
            digit_counts[ch] += 1

with open(output_file, 'w') as report:
    for digit in sorted(digit_counts.keys()):
        report.write(f"{digit} {digit_counts[digit]}\n")
