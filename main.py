from stats import count_words
import os
def main ():
    filepath = os.path.expanduser("~/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt")
    num_words = count_words(filepath)
    print(f"{num_words} words found in the document")

main()
