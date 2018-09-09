import requests
import random
import os

# a hangman-inspired game that randomly grabs a word from the system dictionary then asks the user to guess it letter by letter

clear = lambda: os.system('clear')

# gets word from my system dictionary (will only work on unix systems)
def get_word():
    word_file = "/usr/share/dict/words"
    words = open(word_file).read().splitlines()
    word = random.choice(words)
    while '\'' in word:
        word = random.choice(words)
    return word

# clears the console then updates correctly guessed letters or number of missed tries
def update_display(word, guessed, tries):
    clear()
    print("Welcome to spaceman.\nI'm thinking of a word with this many letters:")
    # initializes the empty spaces
    display = ["_ "] * len(word)
    index = 0
    # guessed is a list of bools that tell you which letters have been guessed
    for item in guessed:
        if item:
            display[index] = word[index]
        index += 1
    display = ''.join(display)
    print(display)
    print("Number of tries: ", tries)

# makes sure the input is a single character
def sanitize_guess(guess):
    if type(guess) is not str:
        return False
    elif len(guess) > 1:
        return False
    else:
        return True

# checks if the guessed letter is in the word and then updates the list of guessed words
def update_discovered(word, guess, already_guessed):
    discovered = already_guessed
    index = 0
    for letter in word:
        if guess in letter:
            discovered[index] = True
        index += 1
    return discovered

# plays the game!
def play_game():
    # keeps track of missed tries
    tries = 0
    # grabs a word and makes it all uppercase
    word = get_word().upper()
    # the list of bools that keeps track of which letters have been guessed
    guessed = [False] * len(word)
    # initializes the display
    update_display(word, guessed, tries)
    # while the 'guessed' list contains False, some words have not been guessed
    while False in guessed:
        guess = input("Guess a letter > ").upper()
        # if the input is valid and a correct guess
        if sanitize_guess(guess) and guess in word:
            guessed = update_discovered(word, guess, guessed)
            update_display(word, guessed, tries)
        # else increment tries
        else:
            tries += 1
            update_display(word, guessed, tries)
            
play_game()