#########################################################################################
# password_generator.py                                                                 #
# Creates a password with certain amount of letters, numbers, and special characters    #
# @author: Elana Aronson                                                                #
#########################################################################################

import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '_', '?']

# User input
number_amount = int(input('How many numbers would you like? \n'))
letter_amount = int(input('How many letters would you like? \n'))
special_amount = int(input('How many special characters would you like? \n'))

# Get the random characters
get_characters = ''
for i in range(0, number_amount):
    get_characters += random.choice(numbers)

for i in range(0, letter_amount):
    get_characters += random.choice(letters)

for i in range(0, special_amount):
    get_characters += random.choice(special_chars)

print(get_characters)

