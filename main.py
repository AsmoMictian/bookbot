def get_book_text(file_path): #takes filepath to text file and opens it. Storing the file in a var.
    thewholebook = ""
    with open(file_path) as f:
        thewholebook = f.read()

    return thewholebook

def main():
    fp = "/home/asmodeus/bookbot/books/frankenstein.txt"
    book = get_book_text(fp)
    print(book)
    return

main()
