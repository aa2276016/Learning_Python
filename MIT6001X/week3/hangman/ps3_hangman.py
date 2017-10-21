# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
            break
    else:
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ''
    for i in secretWord:
        if i in lettersGuessed:
            guess = guess + i + ' '
        else:
            guess = guess + '_ '
    return guess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z']
    available_letters = ''

    for i in letter_list:
        if i not in lettersGuessed:
            available_letters += i

    return available_letters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # show the secret word length
    print('Welcome to the game Hangman!')
    print('\nI am thinking of a word that is', len(secretWord), 'letters long')
    print('___________')

    show_target = '_ ' * len(secretWord)
    print('Your need to guess this word:', show_target)

    guess_list = []
    guess_count = 1
    guess_left = 8

    print('You have 8 guesses left!!')
    while guess_count <= 8:
        # To create an input for guessing the letter
        while True:
            letter_guess = input('\nPlease guess a letter:')
            letter_guess = letter_guess.lower()
            if len(letter_guess) > 1:
                print('\nPlease only input one letter')
                continue
            if letter_guess not in guess_list:
                guess_list.append(letter_guess)
                break
            else:
                print('\nYou have already tried this letter before')
                continue
        guess_count += 1
        # show the inputted guess
        if letter_guess in secretWord:
            print('\nGood guess!')
        else:
            print('\nSorry, it was wrong')

        print('This letter is:', end=' ')
        print(getGuessedWord(secretWord, guess_list))

        # End the game after winning
        if isWordGuessed(secretWord, guess_list):
            guess_count = 10
            print("\nCongratulations! You've WON !!")
            continue

        # remind the available letters
        guess_left -= 1
        print('You have', guess_left, 'guesses left')

    # End the game if guess over 8 times
    if guess_count == 9:
        print("\nSorry, you've lost the game!!")

secretWord = 'apple'
hangman(secretWord)







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
