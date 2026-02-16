def printFibonacci(length):
    num1 = 0
    num2 = 1
    print(f"{num1}\n{num2}")
    while length > 2:
        total = num1 + num2
        print(f"{total}")
        num1 = num2
        num2 = total
        length -= 1


printFibonacci(12)