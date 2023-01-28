# import random
# define a function that simulates rolling a dice
# create a dictionary to store the drawing sof the dice

import random

def roll_dice():
    
    roll = input("Roll the dice? (y/n): ")

    while roll.low() == "y":
        print(random.randint(1,6))
        roll = input("Roll the dice? (y/n): ")