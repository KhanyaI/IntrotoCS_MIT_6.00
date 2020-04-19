# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return (wordlist)

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return (random.choice(wordlist))

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
word = choose_word(wordlist)
word = word.lower()
print(word)
length  = len(word) 
guessed_word = ("_ " * length).split() 
guess_allowed = 7
print (" ".join(guessed_word)) 
while True:
    input_letter = input("Give a letter: ")

    if (input_letter not in word):
        #if letter not in used_lets:
            guess_allowed -= 1 
            if guess_allowed == 0:
                print ("Sorry you lost, the word was:", word)
                break
            print ("Try again, you have only %r lives left!" % guess_allowed)
           

    else:
        for i in range(length):
            if input_letter == word[i]:
                guessed_word[i] = input_letter

    if "".join(guessed_word) == word: #Making it a string again
        print (word + " you guessed it!")
        break










