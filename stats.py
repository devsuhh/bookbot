def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    full_text = text.split()
    words = len(full_text)
    return words

def character_count(text):
    char_count = {}
    for char in text:
        char =  char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters(char_dict):
    sorted_list = []

    for key, value in char_dict.items():
        if key.isalpha():
            sorted_list.append({
                "char": key,
                "num": value
            })
    
    def sort_on(item):
        return item ["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



