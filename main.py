def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    char_list = sort_on(num_chars)
    char_list.sort(reverse=True, key=sort_key)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")
    for char in char_list:
        print(f"The '{char['char']}' character was found {char['count']} times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
      with open(path) as f:
        return f.read()
        
def get_num_characters(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
            if char.isalpha():
                if char in char_dict:
                        char_dict[char] += 1
                else:
                        char_dict[char] = 1
    return char_dict

def sort_on(char_dict):
     char_list = []

     for key,value in char_dict.items():
          char_dict = {"char":key,"count":value}
          char_list.append(char_dict)
     return char_list

def sort_key(char_dict):
    return char_dict["count"]

main()