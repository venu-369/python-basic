import random


exit = False

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Enter your choice or exit: ").lower()
    computer_choice = random.choice(options)
    

    if user_input == "exit":
        exit = True
        print("Thanks for playing!")