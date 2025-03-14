def count_words (filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    words = file_contents.split() 
    return len(words)
