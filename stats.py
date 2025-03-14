# ---------------------------------> import libraries
import os
# ---------------------------------> read book file
def read_book (filepath):
    filepath = os.path.expanduser(filepath)
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents
# ---------------------------------> count words in book
def count_words (filepath):
    words = read_book(filepath).split()
    return len(words)
# ---------------------------------> count characters
def count_individual_chars (filepath):
    filepath = os.path.expanduser(filepath)
    book = read_book(filepath).lower()
    chars_dict = {}
    for char in book:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict
# ---------------------------------> sorting function
def sort_dict(chars_dict):

    return
# ---------------------------------> Test the function
def test():
    path = os.path.expanduser("~/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt")
    print (count_words(path))
    print (count_individual_chars(path))

#test()