# import random
# define a function that simulates rolling a dice
# create a dictionary to store the drawing sof the dice

import random

def roll_dice():
    
    roll = input("Roll the dice? (y/n): ")

    while roll == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("dice rolled: {} and {}".format(dice1, dice2))

        roll = input("Roll again? (y/n): ")

roll_dice()