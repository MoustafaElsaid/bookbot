# ---------------------------------> import
from stats import count_words
from stats import count_individual_chars
from stats import sort_it_out
import os
# ---------------------------------> main function
def main ():
    filepath = os.path.expanduser("~/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt")
    num_words = count_words(filepath)
    chars = count_individual_chars(filepath)
    chars_sorted = sort_it_out(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted:
        char = item["key"]
        number = item["value"]
        if char.isalpha():
            print(f"{char}: {number}")
    print("============= END ===============")
main()
