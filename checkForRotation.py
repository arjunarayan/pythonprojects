"""
Check if two strings are rotations and return true or false
"""

def checkRotation(s1, s2): # Fn definition
    if len(s1) != len(s2): #Checks if the two lengths aren't equal so that it can already return false
        return False
    else: # Duplicates s1 and checks if s2 is in s3 (s1 + s1)
        s3 = s1 * 2
        print(s3)
        if s2 in s3:
            return True
        return False


print(checkRotation("hello", "llohe")) # Calling fn