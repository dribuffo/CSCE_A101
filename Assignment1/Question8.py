'''Imagine you are creating a dictionary to store information about books. Each book should have a
unique ISBN (International Standard Book Number) as the key and should include information about
the book's title and author. Explain how you can use dictionaries to store and manage this information, 
including adding new books, updating book information, and checking if a book exists in the dictionary.
Provide a brief description of each task.'''


# Dictionaries would be a good choice to use for this subject since they store information as a 
# key/value pair. The key would be the ISBN and the value that it's paired with would be the 
# title of the book and author's name. Another benefit to using a dictionary is that you can store
# a lot of data within a list and use the list as a value. That way you can reference either just
# the whole value or parts of the value as needed.

# Dictionary = {Key : Value}, creating a make believe dictionary called bookshelf. Contains
# made up ISBNs as keys and made up titles and authors for values.
bookshelf = {1000 : ["The Joy of Fried Rice", "Uncle Roger"], 157 : ["Your Pokemon and You", "Ash Ketchum"]}

# how to add additional entries: add an entry by updating the dictionary to include
# a new ISBN and assign the list of information to that.
bookshelf[5325] = ["Dragon Slaying 101", "Saint George"]

# updating entry by first locating the book you want to change, then the speciic data within
# the book that you want to update.
# example updating "Your Pokemon and You" author to be Professor Oak
bookshelf[157][1] = "Professor Oak"

# check that a book exists within the library by simply trying to access the information
# first get the ISBN we are looking for from the user, then we check the bookshelf dictionary
# to check for a specific entry and return a message if it exists.
searched_isbn = int(input("What is the ISBN of the book you're looking for? "))

if searched_isbn in bookshelf.keys():
    print(f' "{bookshelf[searched_isbn][0]}" (ISBN:{searched_isbn}) is in the bookself.')
else:
    print(f"Book with ISBN:{searched_isbn} is not in the bookshelf.")