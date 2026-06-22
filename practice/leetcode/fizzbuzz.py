from time import *
def fizzbuzz(num):
    start = time()
    if num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    else:
        print("not divisible by 3 or 5")
    end = time()
    print(f"Time taken to run the code was {end - start} seconds")

fizzbuzz(25)
