import sys
import codecs

if len(sys.argv) != 2:
  print("please give file name")
  exit()

filename = sys.argv[1]
with open(filename, 'r') as fh:
    original = fh.read()

encoded = codecs.encode(original, encoding='rot_13')

with open(filename, 'w') as fh:
    fh.write(encoded)
