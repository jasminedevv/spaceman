import requests
import random
import os

clear = lambda: os.system('clear')

def get_word():
    word_file = "/usr/share/dict/words"
    words = open(word_file).read().splitlines()
    word = random.choice(words)
    while '\'' in word:
        word = random.choice(words)
    return word

def update_display(word, guessed, tries):
    clear()
    print("Welcome to spaceman.\nI'm thinking of a word with this many letters:")

    display = ["_ "] * len(word)
    index = 0
    for item in guessed:
        if item:
            display[index] = word[index]
        index += 1
    display = ''.join(display)
    print(display)
    print("Number of tries: ", tries)

def sanitize_guess(guess):
    if type(guess) is not str:
        return False
    elif len(guess) > 1:
        return False
    else:
        return True

def update_discovered(word, guess, already_guessed):
    discovered = already_guessed
    index = 0
    for letter in word:
        if guess in letter:
            discovered[index] = True
        index += 1
    return discovered

def play_game():
    tries = 0
    word = get_word().upper()
    guessed = [False] * len(word)
    update_display(word, guessed, tries)
    while False in guessed:
        guess = input("Guess a letter > ").upper()
        if sanitize_guess(guess) and guess in word:
            guessed = update_discovered(word, guess, guessed)
            update_display(word, guessed, tries)
        else:
            tries += 1
            update_display(word, guessed, tries)
            
    print("\n")

def test():
    # print(sanitize_guess('n'))
    # print(sanitize_guess(4))
    # print(sanitize_guess('ne'))
    print(find_letters("ababa", 'a'))


play_game()
# test()