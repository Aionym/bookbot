import sys
from pathlib import Path
from stats import number_of_words, get_book_text, letters_count, sorted_letters


def main():
    if  len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = Path(sys.argv[1])
    book_text = get_book_text(book_path)
    number_words = number_of_words(book_text)
    number_letters = letters_count(book_text)
    sorted_count = sorted_letters(number_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()