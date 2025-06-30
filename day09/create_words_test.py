from word_counter import read_file, count_words

def test_read_file(tmp_path):
    # Create a temporary test file
    file = tmp_path / "sample.txt"
    file.write_text("Hello World\nSecond Line")

    result = read_file(str(file))
    assert result == ["hello world", "second line"]

def test_count_words_simple():
    lines = ["hello world", "hello again"]
    result = count_words(lines)
    assert result["hello"] == 2
    assert result["world"] == 1
    assert result["again"] == 1

def test_count_words_empty_line():
    lines = ["", "     ", "word"]
    result = count_words(lines)
    assert result["word"] == 1
    assert len(result) == 1
