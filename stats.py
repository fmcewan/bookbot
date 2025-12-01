def sort_on(items):

    return items["num"]

def get_num_words(string_text):

    words = string_text.split()
    num_words = len(words)

    return f"Found {num_words} total words"

def count_characters(string_text):

    text =  string_text.lower()
    char_count = {}

    for ch in text:
        if ch not in char_count:
            char_count[ch] = 0
        char_count[ch] += 1

    return char_count

def sort_dictionary(count_dict):
   
    dictionary_list = []
    for key in count_dict:
        char_dict = {}
        
        char_dict["char"] = key
        char_dict["num"] = count_dict[key]
        
        dictionary_list += [char_dict]

    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list

