def main():
    file_path = 'books/frankenstein.txt'
    
    # Read the file and return the data
    book_text = read_book(file_path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)
    # Debugging code remove me
    print(f'{word_count} total words')
    print_report(file_path, word_count, char_dict)
    
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
    
    for char in input.lower():
        if not(char.isalpha()):
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def print_report(file, wc, char_dict):
    print(f'--- Begin report of {file} ---')
    print(f'{wc} words found in the document', end='\n\n')
    
    for char in convert_dict_to_sorted_list(char_dict):
        print(f'The \'{char['char']}\' character was found {char['count']} times')
    
    print(f'--- End report ---')
    
def convert_dict_to_sorted_list(dict):
    sorted_list = []
    for key in dict:
        sorted_list.append({"char": key, "count": dict[key]})
        
    sorted_list = sorted(sorted_list, key=lambda a:a["count"], reverse=True)
    
    return sorted_list
if __name__ == '__main__':
    main()