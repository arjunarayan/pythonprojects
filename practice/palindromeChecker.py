def checkPalindrome(s):
    new_s = ""
    for i in range(len(s)-1, -1, -1):
        new_s += s[i]
    if s == new_s:
        return True
    else:
        return False


print(checkPalindrome("academymedaca"))