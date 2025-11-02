from stats import word_count
from stats import char_count
from stats import clean_dict
from stats import sort_on
from stats import num_sort
import sys


def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    return word_count(get_book_text(text))

def out():
    if len(sys.argv) == 2:
        text = str(sys.argv[1])
        x = num_sort(clean_dict((char_count(get_book_text(text)))))
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at books/frankenstein.txt...")
        print(f"----------- Word Count ----------")
        print(f"Found {word_count(get_book_text(text))} total words")
        print(f"--------- Character Count -------")
        for item in x:
            if item["char"].isalpha() == True:
                print(f"{item["char"]}: {item["num"]}")
        print(f"============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
out()

