################################################################
# game.py                                                      #
# Hangman game functions                                       #
# @author: Elana Aronson                                       #
################################################################

# Private package
import data

#Public packages
import random

# Word set up
def get_word():
    word = random.choice(data.words)
    return word

def get_word_length(word):
    return len(word)

def blank_space_word(length):
    return ['_'] * length

def letter_hash_map(word):
    letter_map = {}
    for i, letter in enumerate(word):
        if letter not in letter_map:
            letter_map[letter] = [i]
        elif letter in letter_map:
            letter_map[letter].append(i)
    return letter_map

# User input
def mode():
    return input("What mode would you like to play? (easy, medium, or hard)\n")

def guess_letter():
    return input("What letter would you like to guess? \n")

# Guess
def right_guess(letter_hash, letter, blank_word):
    for index in letter_hash[letter]:
        blank_word[index] = letter
    return blank_word


    

guess = 6
d = {'a':[0]}
b = blank_space_word(1)
while guess != 0 or '_' not in b:
    letter = guess_letter()
    if letter in d:
        b = right_guess(d, letter, b)
    else:
        guess -= 1
    print(b, guess)


