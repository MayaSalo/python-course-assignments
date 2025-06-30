from collections import defaultdict

def read_file(filename):
    """Reads a file and returns its lines."""
    with open(filename, 'r') as fh:
        return [line.rstrip('\n').lower() for line in fh]

def count_words(lines):
    """Counts words from a list of lines and returns a word frequency dictionary."""
    count = defaultdict(int)
    for line in lines:
        for word in line.split():
            if word:
                count[word] += 1
    return count

def display_word_counts(counts):
    """Displays word counts in a sorted, formatted table."""
    for word in sorted(counts):
        print("{:13} {:>2}".format(word, counts[word]))
