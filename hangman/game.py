################################################################
# game.py                                                      #
# Hangman game                                                 #
# @author: Elana Aronson                                       #
################################################################

# Private package
import data

#Public packages
import random

def get_word():
    word = random.choice(data.words)
    return word

def get_word_length(word):
    return len(word)

def blank_space_word(length):
    return ['_'] * length

def letter_hash_map(word):
    letter_map = {}
    for i, char in enumerate(word):
        if char not in letter_map:
            letter_map[char] = [i]
        elif char in letter_map:
            letter_map[char].append(i)
    return letter_map


