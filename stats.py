# Function that gets book word count
def num_words(book_text):
    # split book into individual words
    words_in_book = book_text.split()
    # count words
    word_count = len(words_in_book)
    # return word_count
    return word_count

# Function that counts the number of occurences of each character in a book
def count_chars(book_text):
    # define dictionary of unique characters
    unique_chars = {}
    # loop through all characters in book
    for char in book_text:
        # checks whether or not each character is not in unique characters dictionary
        if char.lower() not in unique_chars:
            # if it is not present, it is added as a key and this first instance is counted
            unique_chars[char.lower()] = 1
        # otherwise
        else:
            # the count of that character is increased in the dictionary
            unique_chars[char.lower()] += 1

# slower way, method removed.    
#    for key in unique_chars:
#        for char in book_text:
#            if char == key:
#                unique_chars[key] += 1

    # returns the unique character dictionary
    return unique_chars

# Function that conversts a dictionary of characters and quantity into a sorted list of dictionaries
def sort_chars(unique_chars):
    # define list
    char_list = []
    # loop through each key in dictionary
    for key in unique_chars:
        # create a temporary dictionary for each character / quantity
        tmp_dict = {"char": key, "num": unique_chars[key]}
        # add dictionary to list
        char_list.append(tmp_dict)
    
    # sort list of dictionaries
    char_list.sort(reverse=True, key=sort_on)
    # returns the list of dictionaries
    return char_list

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]