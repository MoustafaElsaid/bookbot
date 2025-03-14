from stats import count_words
def main ():
    filepath = "/Users/moustafaelsaid/Documents/Studies/Coding/Boot.Dev/github.com/bookbot/books/frankenstein.txt"
    # book_text = get_book_text(filepath)
    num_words = count_words(filepath)
    print(f"{num_words} words found in the document")

main()
