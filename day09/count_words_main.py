import sys
from word_counter import read_file, count_words, display_word_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    lines = read_file(filename)
    word_counts = count_words(lines)
    display_word_counts(word_counts)

if __name__ == "__main__":
    main()
