def printFibonacci(n):
    num1 = 0
    num2 = 1
    print(f"{num1}\n{num2}")
    while n > 2:
        total = num1 + num2
        print(total)
        num1 = num2
        num2 = total
        n -= 1



printFibonacci(9)