################################################################
# treasure_island.py                                           #
# Treasure Island game to complete a quest to find treasure:   #
# If you go through the correct way, you win else game over    #
# @author: Elana Aronson                                       #
################################################################

# Welcome message to the treasure quest game
print("Welcome to Treasure Island.\nYour mission is to find the treasure")

#First Quest
first_quest = input('You are at crossroads, where do you want to go? ' 
                    'Left or right?\n').lower()
if first_quest == 'left':

    #Second Quest
    second_quest = input('You have come to a lake. '
                         'There is an island in the middle of the lake. '
                          "Type 'swim' to swim across "
                          "or type 'wait' to wait for the boat\n").lower()
    if second_quest == 'wait':

        #Third Quest
        third_quest = input("You have arrived to the island unharmed. "
                            "There is a house with three doors? "
                            "Which door do you choose: Blue, Yellow, or Red?\n").lower()
        if third_quest == 'yellow':
            print('You Win!')
        elif third_quest == 'blue':
            print("Eaten by beasts. Game Over")
        elif third_quest == 'red':
            print("Burned by fire. Game Over")
        else:
            print("Game Over")

    else:
        print("Attacked by trout. Game Over")

else:
    print('Fell into the hole. Game Over')
