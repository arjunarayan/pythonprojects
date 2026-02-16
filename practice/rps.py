from rpsRigged import *
from random import choice

choices = ["rock", "paper", "scissors"]
userChoice = ""


def rpsplay(name, user):
    computer_choice = choice(choices)
    name = input("What's your name?")
    if user == "rock":
        if computer_choice == "rock":
            print( "Draw!")
        elif computer_choice == "paper":
            print("You lose!") 
        else:
            print("You win!") 
    elif user == "paper":
        if computer_choice == "paper":
            print("Draw!")
        elif computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user == "scissors":
        if computer_choice == "scissors":
            print("Draw!")
        elif computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Bro, you chose something invalid!")



userName = input("What's your name?")
rpsPlay(userName)



