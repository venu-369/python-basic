import random


exit = False
user_points = 0
computer_points = 0

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
                computer_points += 1
            elif computer_choice == "scissors":
                print("Computer chose scissors. You win!")
                user_points += 1

        elif user_input == "paper":
            if computer_choice == "rock":
                print("Computer chose rock. You win!")
                user_points += 1
            elif computer_choice == "paper":
                print("Computer chose paper. It's a tie!")
            elif computer_choice == "scissors":
                print("Computer chose scissors. You lose!")
                computer_points += 1

        elif user_input == "scissors":
            if computer_choice == "rock":
                print("Computer chose rock. You lose!")
                computer_points += 1
            elif computer_choice == "paper":
                print("Computer chose paper. You win!")
                user_points += 1
            elif computer_choice == "scissors":
                print("Computer chose scissors. It's a tie!")
        
        print("Your score: " + str(user_points))
        print("Computer score: " + str(computer_points))

   
        
        if user_points > computer_points:
            print("You won!")
        elif user_points < computer_points:
            print("You lost!")
        elif user_points == computer_points:
            print("It's a tie!")

