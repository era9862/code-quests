################################################################
# rock_paper_scissor.py                                        #
# Game of Rock Paper Scissor                                   #
# @author: Elana Aronson                                       #
################################################################

import random

# Welcome message
print("Welcome to the game of Rock Paper Scissor")

choice_list = ['rock', 'paper', 'scissor']

# Computer randomly choose either rock, paper, or scissor
computer_choice = random.choice(choice_list) 

# Start of the game(
user_choice = input("Please select either rock, paper or scissor ").lower()

if user_choice not in choice_list:
    print('Invalid answer')

else:

    # Display the user's and computer's choice
    print(f'You chose {user_choice}')
    print(f'Computer chose {computer_choice}')

    # User's results

    # Tie
    if user_choice == computer_choice:
        print('Its a draw')

    # Lose
    if computer_choice == 'rock' and user_choice == 'scissor':
        print('Computer win')
    if computer_choice == 'paper' and user_choice == 'rock':
        print('Computer win')
    if computer_choice == 'scissor' and user_choice == 'paper':
        print('Computer win')

    # Win
    if user_choice == 'rock' and computer_choice == 'scissor':
        print('You win')
    if user_choice == 'paper' and computer_choice == 'rock':
        print('You win')
    if user_choice == 'scissor' and computer_choice == 'paper':
        print('You win')