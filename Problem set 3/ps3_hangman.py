# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    # FILL IN YOUR CODE HERE...
    for char in lettersGuessed:
        if(secretWord.find(char) == -1):
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    unfiniWord = list('_' * len(secretWord))
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            unfiniWord[i] = secretWord[i]
    return ''.join(unfiniWord)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = list(string.ascii_lowercase)
    finishAlphabet = []
    for char in alphabet:
        if char not in lettersGuessed:
            finishAlphabet.append(char)
    return ''.join(finishAlphabet)


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
    # FILL IN YOUR CODE HERE...
    win = False
    lenght = len(secretWord)
    print('The secret word has : ' + str(lenght) + ' letters')
    trys = 8
    guesses = []
    print(secretWord)

    while not win and trys > 0:
        print('Te quedan ' + str(trys) + ' intentos')
        print('Estas son las letras que tienes disponibles: ' +
              getAvailableLetters(guesses))
        guess = input('Write a letter : ')
        if guess in list(getAvailableLetters(guesses)):
            guesses.append(guess)
            if isWordGuessed(secretWord, list(guess)):
                print('Letra correcta, ' + getGuessedWord(secretWord, guesses))
            else:
                print('Letra incorrecta : ' +
                      getGuessedWord(secretWord, guesses))
                trys -= 1
            if secretWord == getGuessedWord(secretWord, guesses):
                return print('Has ganado bro')
        else:
            print('Esa letra ya la has introducido')
    return print('Bua malisimo')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
