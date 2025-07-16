from random import *

num = randint(1, 10)


def check():
    tries = 0
    while tries < 3:
        user_input = int(input("Try to guess a number between 1 and 10: "))
        if 10 >= user_input > 0:
            if user_input == num:
                print("Bro, you didn't get it! Just Kidding! You got it!")
                return
            elif user_input > num:
                print("Too High! Too High! Too High! Too High! Too High! Too High!")
            elif user_input < num:
                print("Too low! Too low! Too low! Too low! Too low! Too low!")
            tries += 1
        else:
            print("Please put in something valid.")
    print(f"No more guesses!\nThe correct number was {num}")

check()

