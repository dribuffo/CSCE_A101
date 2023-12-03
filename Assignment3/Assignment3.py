'''
Daniel Ribuffo - Assignment 3 
CSCE A 101 - FA23
'''

'''
Step 1. Read in the file that I provide to you, words.txt:
Used the code provided to input the file contents as a singular string.
'''
f = open('words.txt', 'r') # open the file for reading
contents = f.read() # read the entire file contents as one big string
f.close() # close the file

'''
Step 2. Extracting the 5 letter words from the .txt file:
Splits the 'contents' into a list by splitting the string every space,
then adds all the words of 5 letter length into a list.
'''
contents = contents.split()
five_letter_words = [x for x in contents if len(x) == 5]

'''
Step 3. Calculate the frequency distribution of the letters:
Create a dictionary that contains all 26 letters of the alphabet, 
then a nested loop pair will loop over each word and then each letter and add
it to the dictionary who will keep count of the frequency
'''
alphabet = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,"g": 0, "h": 0, "i": 0, "j": 0,
    "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, 
    "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
}

for word in five_letter_words:
    for letter in word:
        if letter in alphabet:
            alphabet[letter] = alphabet.get(letter) + 1

#mandatory printout of values for a, s, and q:
print(f"a = {alphabet.get('a')}")
print(f"s = {alphabet.get('s')}")
print(f"q = {alphabet.get('q')}")
'''
Step 4. Calculate a score for each word that is the sum of its letter frequencies:
I created an empty dictionary and then looped through each word in the list of words.
Using the dictionary I created in the last step I used the values of each letter to add
to a new variable that will get added to the empty dictionary as the value with the key being
the word we are on. From there the variable resets to 0 for every word to start the calculation
all over.
'''
word_score = {}
for word in five_letter_words:
    sum_of_word = 0
    for letter in word:
        if letter in alphabet:
            sum_of_word += alphabet.get(letter)
    word_score[word] = sum_of_word
'''
Step 5. Print 5 words that maximize the number of high-frequency letters:
I used the .items() function to create a list of tuples that is (word, word_score). From there
I used a list comprehension to create a list that reversed the tuples so that they are (word_score, word).
Then I used .sorted() to sort them by descending order w/ reverse = True. Then I printed them out w/ a loop. 
'''
keys_and_values = word_score.items()
reversed_word_score = [(item[1], item[0]) for item in keys_and_values]
reversed_word_score = sorted(reversed_word_score, reverse=True)
print("Top 5 guesses:")
for x in range(5):
    if x == 4:
        print(reversed_word_score[x])
    else:
        print(reversed_word_score[x], end=', ')

'''
Bonus: Print the 5 words with unique letters that maximize the number of high-frequency letters.
Using the provided function, I looped through the list created in step 5 to find the first 5
words that are made of unique letters that have the highest scores and then I printed them.
'''
def unique_chars(word):
    '''Return True if all characters in word are unique, else False'''
    chr_exists = [False] * 128
    for ch in word:
        unicode_val = ord(ch)
        if chr_exists[unicode_val]:
            return False
        chr_exists[unicode_val] = True
    return True

print("These are the top highest scoring words with unique letters:")
i = 0
for j in reversed_word_score:
    if i < 5:  
        if unique_chars(j[1]) == True:
            print(f"{j[1]} has a score of {j[0]}")
            i += 1
    else:
        break