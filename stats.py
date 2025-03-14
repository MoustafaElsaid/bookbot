import os
def count_words (filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split() 
    return len(words)
def test():
    path = os.path.expanduser("~/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt")
    print (count_words(path))

test() 