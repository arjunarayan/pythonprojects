def checkPalindrome(str_input):
    str_input = str_input.lower()
    input_backwards = ""
    for index in range(len(str_input)-1, -1, -1):
        input_backwards += str_input[index]
    return str_input == input_backwards


print(checkPalindrome("dad"))

def checkPalindrome(str_input):
    i = 0
    j = len(str_input)-1
    while i < j:
        if str_input[i] != str_input[j]:
            return False
        i += 1
        j -=1
    return True