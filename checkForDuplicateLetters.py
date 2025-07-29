def checkForDuplicates(word): # defining fn
    seen = set() # Initializing array called seen. This stores all letters seen.
    for char in word: # For loop going through each character in word
        if char in seen:
            return False
        seen.add(char)
    return True
        # It checks if the current letter already in seen. If true, it'll return false. Otherwise, it'll append it to seen, and restart the loop.
        # If it's iterated through the whole word, and it still hasn't exited the function, it'll return true.

print(checkForDuplicates("qwertyuiopasdfghjklzxcvbnm"))
