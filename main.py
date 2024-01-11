def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path).lower()
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    print(f'--- Begin report of {book_path} ---')
    print(f"{num_words} words found in the document\n\n")
    dict_to_list = list(letter_count.items())
    
    letter, count = zip(*sorted(dict_to_list))
    for i in range(len(letter)):
      print(f"The '{letter[i]}' character was found {count[i]} times")
    
    print('--- End report ---')
      
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_letter_count(text):
    dict = {}
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    for letter in text:
      if letter in alphabet and letter not in dict.keys():
        dict[letter] = 1
      elif letter in alphabet and letter in dict.keys():
        dict[letter] += 1
    return dict


    
    
    
main()