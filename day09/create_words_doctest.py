from collections import defaultdict

def read_file(filename):
    """
    Reads a file and returns a list of lines in lowercase, with newlines removed.

    Args:
        filename (str): Path to the text file.

    Returns:
        list[str]: List of cleaned lines in lowercase.

    Example:
        >>> with open("testfile.txt", "w") as f:
        ...     _ = f.write("Hello World\\nSecond Line")
        >>> read_file("testfile.txt")
        ['hello world', 'second line']
    """
    with open(filename, 'r') as fh:
        return [line.rstrip('\n').lower() for line in fh]

def count_words(lines):
    """
    Counts word occurrences in a list of lines.

    Args:
        lines (list[str]): Lines of text.

    Returns:
        dict[str, int]: Dictionary mapping words to their frequency.

    Example:
        >>> lines = ["hello world", "hello again"]
        >>> sorted(count_words(lines).items())
        [('again', 1), ('hello', 2), ('world', 1)]
    """
    count = defaultdict(int)
    for line in lines:
        for word in line.split():
            if word:
                count[word] += 1
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
