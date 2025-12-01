import sys

from stats import get_num_words, count_characters, sort_dictionary

def get_book_text(file_path):
    
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():

    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text_file_path = sys.argv[1]
    text = get_book_text(text_file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_file_path}...")
    
    print("----------- Word Count ----------")

    print(get_num_words(text))
    
    print("--------- Character Count -------")

    dictionary_list = sort_dictionary(count_characters(text))

    for dictionary in dictionary_list:
        char = dictionary["char"]
        num = dictionary["num"]
        
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()
