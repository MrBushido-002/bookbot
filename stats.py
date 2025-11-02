def word_count(book):
    words = book.split()
    return len(words)

def char_count(book):
    letter_dict = {}
    char = list(book)
    for item in char:
        if item.lower() in letter_dict:
            letter_dict[item.lower()] += 1
        else:
            letter_dict[item.lower()] = 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def clean_dict(dict):
    nice_list = []
    for key in dict:
        nice_list.append({"char": key, "num": dict[key]})
    return nice_list

def num_sort(list):
    list.sort(reverse=True, key=sort_on)
    return list

