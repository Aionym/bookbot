def get_book_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents


def number_of_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def letters_count(book_text):
    let = {}
    for t in book_text:
        char = t.lower()
        if char in let:
            let[char] += 1
        else:
            let[char] = 1
    return let

def sort_on(item):
    return item["num"]

def sorted_letters(number_letters):
    letters_list = []
    for char, count in number_letters.items():
        if char.isalpha():
            items = {"char": char, "num": count}
            letters_list.append(items)
    letters_list.sort( reverse=True, key=sort_on)
    return letters_list

