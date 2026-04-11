import random

number = random.randint(1, 100)

while True:
    number1 = int(input("Choose number (1-100): "))
    if number < number1:
        print("Too high")
    if number > number1:
        print("Too low")
    if number == number1:
        print("correct")
        break
