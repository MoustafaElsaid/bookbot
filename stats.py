import os
def read_book (filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents
def count_words (filepath):
    words = read_book(filepath).split()
    return len(words)

def test():
    path = os.path.expanduser("~/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt")
    print (count_words(path))

test() 