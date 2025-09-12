def checkIfIntPalindrome(num):
    original = num
    result = 0
    while num > 0:
        rem = num % 10
        result = result * 10 + rem
        num = int(num/10)

    if result == original:
        return True
    else:
        return False

print(checkIfIntPalindrome(5115))