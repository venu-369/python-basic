import random


exit = False

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Enter your choice or exit: ").lower()
    computer_choice = random.choice(options)
    

    if user_input == "exit":
        print("Thanks for playing!")
        exit = True

        if user_input == "rock":
            if computer_choice == "rock":
                print("Computer chose rock. It's a tie!")
            elif computer_choice == "paper":
                print("Computer chose paper. You lose!")
            elif computer_choice == "scissors":
                print("Computer chose scissors. You win!")