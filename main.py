def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words (filepath):
    words = get_book_text(filepath).split()
    return len(words)
    
def main ():
    filepath = "/Users/moustafaelsaid/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt"
    # book_text = get_book_text(filepath)
    num_words = count_words(filepath)
    print(f"{num_words} words found in the document")

main()
