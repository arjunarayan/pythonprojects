import random
from random import choice

choices = ["rock", "paper", "scissors"]
userChoice = ""

def checkWin(user, computer):
    if user == "rock":
        if computer == "rock":
            return "Draw!"
        elif computer == "paper":
            return "You lose!"
        else:
            return "You win!"
    elif user == "paper":
        if computer == "paper":
            return "Draw!"
        elif computer == "scissors":
            return "You lose!"
        else:
            return "You win!"
    elif user == "scissors":
        if computer == "scissors":
            return "Draw!"
        elif computer == "rock":
            return "You lose!"
        else:
            return "You win!"
    else:
        return ("Bro, you chose something invalid!"
                "")

while userChoice != "stop":
    computerChoice = choice(choices)
    userChoice = input("Enter rock, paper, or scissors to play rock paper scissors: ")
    if userChoice == "stop":
        break
    print(f"{checkWin(userChoice, computerChoice)} The computer choice was {computerChoice}")




