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
print(first_unique_letter("aabb"))
