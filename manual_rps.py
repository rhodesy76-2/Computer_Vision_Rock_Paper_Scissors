# %%
# Importing random module to allow us to pick a random option between rock, paper, and scissors
import random


# Function to randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
def get_computer_choice():
    choice_list = ("Rock", "Paper", "Scissor")
    computer_choice =  random.choice(choice_list)
    print(f"The computer chose {computer_choice}") 
    return computer_choice


# Function to ask the user for an input and return it.
def get_user_choice():
    while True:
        user_choice = input("Please chose one of Rock, Paper or Scissor") 
        if user_choice == "Rock":
            print("You chose Rock")
            return user_choice 
        elif user_choice == "Paper":
            print("You chose Paper") 
            return user_choice 
        elif user_choice == "Scissor":
            print("You chose Scissor")
            return user_choice 
        else:
            print("Please input a valid input; Rock, Paper or Scissor")


#  Function to chose winner
def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
       print(f"It's a draw, you both chose {computer_choice}")
    elif user_choice == "Rock":
       if computer_choice == "Scissor":
           print("Rock breaks Scissor, you won!")
       else:
           print("Paper covers Rock, you lost!")
    elif user_choice == "Paper":
       if computer_choice == "Rock":
           print("Paper covers Rock , you won!")
       else:
           print("Scissor cuts Paper, you lost!")
    elif user_choice == "Scissor":
       if computer_choice == "Paper":
           print("Scissor cuts Paper , you won!")
       else:
           print("Rock breaks Scissor, you lost!")
           
# get_winner("Rock", "Scissor")    
def play():    
    computer_choice = get_computer_choice()
    input("When ready to play press enter to start 3 second countdown")
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
    
play()

    
# %%
