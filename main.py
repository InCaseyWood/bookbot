# importing functions
from stats import num_words
from stats import count_chars
from stats import sort_chars

# importing sys and modules
import sys
import os

# Function loads book text as a string
def get_book_text(filepath):
    # open file
    with open(filepath) as f:
        #read text
        book_text = f.read()
    # return book as a string
    return book_text

# Function checks and parses arguments
def check_args():
    # check if enough arguments have been given
    if len(sys.argv) < 2:
        # if not, display how to use program and exits
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    # stores argument in path variable
    book_path = sys.argv[1]
    # checks if provided path is valid
    if not os.path.exists(book_path):
        # if path does not exist, informs user and exits
        print(f"{book_path} does not exist.  Please enter a valid path...")
        exit(1)
    # returns path
    return book_path

# Function main
def main():
    # define path to book
    filepath = check_args()
    # call function to get book as string
    book_text = get_book_text(filepath)
    # call function to count number of words in book
    word_count = num_words(book_text)
    # call function to identify unique characters and how often they occur
    unique_chars = count_chars(book_text)
    # call function to sort unique character dictionary into a list of dictionaries sorted by frequency of occurrence
    sorted_chars = sort_chars(unique_chars)

    # print header text
    print("============ BOOKBOT ============")
    # print book being analyzed based on filepath
    print(f"Analyzing book found at {filepath}...")
    # print header for word count
    print("----------- Word Count ----------")
    # print word count
    print(f"Found {word_count} total words")
    # print header for character count
    print("--------- Character Count -------")
    #iterate through list of sorted character dictionaries
    for char_dict in sorted_chars:
        # checks if character is alphabetical
        if char_dict["char"].isalpha():
            # print character and how often it occurs
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    # print tail text
    print("============= END ===============")

# calls the main function
main()