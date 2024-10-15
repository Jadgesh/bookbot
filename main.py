def main():
    file_path = 'books/frankenstein.txt'
    
    # Read the file and return the data
    book_text = read_book(file_path)
    word_count = count_words(book_text)
    # Debugging code remove me
    print(f"{word_count} total words")
    
def read_book(path):
    book_text = None
    
    with open(path, 'r') as file:
        book_text = file.read()
        
    # Close file to avoid corruption
    file.close()
    
    return book_text

def count_words(input):
    return len(input.split())

if __name__ == '__main__':
    main()