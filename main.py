from stats import num_words

def get_book_text(file_path): #takes filepath to text file and opens it. Storing the file in a var.
    thewholebook = ""
    with open(file_path) as f:
        thewholebook = f.read()

    return thewholebook #Returns the whole book as a string.

def main():
    fp = "/home/asmodeus/bookbot/books/frankenstein.txt"
    book = get_book_text(fp)
    decount = num_words(book)
    print(f"{decount} words found in the document")
    return 


main()