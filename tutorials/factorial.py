def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)



print(factorial(6))
print(6*5*4*3*2*1)