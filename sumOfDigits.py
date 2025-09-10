def addSumOfDigits(number : int):
    result = 0
    while number > 0:
        remainder = number % 10
        result += remainder
        number = int(number/10)
    return result


print(addSumOfDigits(1234))