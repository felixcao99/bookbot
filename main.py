from stats import *

def get_book_text(bookpath):
    """
    Extracts the text from a book object.

    Args:
        book: The book object to extract text from.

    Returns:
        str: The extracted text.
    """
    with open(bookpath, 'r', encoding='utf-8') as file:
        book = file.read()
    return book

def main():
    import sys
    """
    Main function to run the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # bookpath = './books/frankenstein.txt'  # Path to the book file
    bookpath = sys.argv[1]  # Get the book path from command line argument
    book_text = get_book_text(bookpath)
    num_words = countwords(book_text)
    num_letters = countletters(book_text)
    sorted_letters = sortedcountlettesnew(num_letters)
    # print(f"{num_words} words found in the document.")
    # print(num_letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        if letter['char'].isalpha():
            print(f"{letter['char']}: {letter['count']}")
    print("============= END ===============")

main()