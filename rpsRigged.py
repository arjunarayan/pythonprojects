def rpsPlay(name):
    print(f"Let's play rock paper scissors, {name}!")
    choice = input("rock, paper, or scissors?")

    if name == "Arjun" or name == "arjun" or name == "ARJUN":
        if choice == "rock":
            print("You win! I chose scissors")
        elif choice == "paper":
            print("You win! I chose rock")
        elif choice == "scissors":
            print("You win! I chose paper!")
        else:
            print("Invalid")
        return ""

    else:
        if choice == "rock":
            print("You lose! I chose paper")
        elif choice == "paper":
            print("You lose! I chose scissors")
        elif choice == "scissors":
            print("You lose! I chose rock")
        else:
            print("Invalid")

        return ""
