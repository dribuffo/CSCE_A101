'''You have a string input_string containing a sentence, write a Python program to find and display the
longest word in the sentence. The string input_string may contain spaces and punctuation.'''

#Get string from user
input_string = input("Please write a sentence: ")

#create comparitor vaariable and assign it to an empty string
longest_word = ''

#this splits the string into a list of words. New list entry is created when it encounters a space.
string_list = input_string.split()

#iterates through the string_list list and compares all the entries with each other to find the longest word.
for words in string_list:
    if len(words) > len(longest_word):
        longest_word = words

#outputs the longest word
print(f'Longest word: {longest_word}')

#I have no idea how you're supposed to do this without using a loop.