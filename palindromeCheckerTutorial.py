def checkPalindrome(input_str):
    lowerString = input_str.lower()
    reversed_string = ""
    for index in range(len(lowerString)-1, -1, -1):
        reversed_string += lowerString[index]
    if reversed_string == lowerString:
        return True
    else:
        return False

if checkPalindrome("hello"):
    print("It's a Palindrome!! Whoop! Whoop!")
else:
    print("Not a palindrome!!! Waah!!")