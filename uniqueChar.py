'''
    Find the first unique character in the string and return the character.
    input: leetcode
    output: l
'''
def first_unique_letter(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter in word:
        if letter_count[letter] == 1:
            return letter
    return ""

# Example
print(first_unique_letter("aabbccddeeffgghhiijjkkllmmnnooppqqrrstuvwxyz"))
