# %%
# Importing random module to allow us to pick a random option between rock, paper, and scissors
import random
choice_list = ("Rock", "Paper", "Scissor")

# Function to randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
def get_computer_choice():
    computer_choice =  random.choice(choice_list)
    print(f"The computer chose {computer_choice}") 
    return computer_choice

get_computer_choice()
# %%
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

get_user_choice()   
  # %%      