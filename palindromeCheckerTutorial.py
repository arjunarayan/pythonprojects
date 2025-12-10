# def checkPalindrome(input_str):
#     lowerString = input_str.lower()
#     reversed_string = ""
#     for index in range(len(lowerString)-1, -1, -1):
#         reversed_string += lowerString[index]
#     if reversed_string == lowerString:
#         return True
#     else:
#         return False
#
# if checkPalindrome("hello"):
#     print("It's a Palindrome!! Whoop! Whoop!")
# else:
#     print("Not a palindrome!!! Waah!!")

def checkPalindrome(input_str: str) -> bool:
    return input_str == input_str[::-1]

print(checkPalindrome("gummy bearss"))