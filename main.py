def main():
    file_path = 'books/frankenstein.txt'
    
    # Read the file and return the data
    book_text = read_book(file_path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)
    # Debugging code remove me
    print(f"{word_count} total words")
    print(char_dict)
    
def read_book(path):
    book_text = None
    
    with open(path, 'r') as file:
        book_text = file.read()
        
    # Close file to avoid corruption
    file.close()
    
    return book_text

def count_words(input):
    return len(input.split())

def count_characters(input):
    char_dict = {}
    
    for char in input:
        if not(char.isalpha()):
            continue
        
        lower_case = char.lower()
        if lower_case in char_dict:
            char_dict[lower_case] += 1
        else:
            char_dict[lower_case] = 1
    
    return char_dict
if __name__ == '__main__':
    main()