celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

unique_words = []
counts = []

for word in celestial_objects:
  
    if word in unique_words:
        index = unique_words.index(word)
        counts[index] += 1
    else:
        unique_words.append(word)
        counts.append(1)

for i in range(len(unique_words)):
    print(f"{unique_words[i]}  {counts[i]}")
