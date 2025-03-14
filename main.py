# ---------------------------------> import
from stats import count_words
from stats import count_individual_chars
import os
# ---------------------------------> main function
def main ():
    filepath = os.path.expanduser("~/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt")
    num_words = count_words(filepath)
    chars = count_individual_chars(filepath)
    print(f"{num_words} words found in the document")
    print(chars)

main()
