# ---------------------------------> import libraries
import os
# ---------------------------------> read book file
def read_book (filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents
# ---------------------------------> count words in book
def count_words (filepath):
    words = read_book(filepath).split()
    return len(words)
# ---------------------------------> count characters
def count_individual_chars (filepath):
    book = read_book(filepath).lower()
    chars_dict = {}
    for char in book:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict
# ---------------------------------> sorting function
def sort_it_out(dict):
    dict_to_list = []
    for key, value in dict.items():
        dict_to_list.append({"key": key, "value" : value})
    def sort_value(dict):
        return dict["value"]
    dict_to_list.sort(reverse=True, key=sort_value)
    return dict_to_list
# ---------------------------------> Test the function
def test():
    path = os.path.expanduser("~/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt")
    print (count_words(path))
    print (count_individual_chars(path))

#test()