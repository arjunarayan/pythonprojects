

def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def checkAnagram(word1, word2):
    wordLower = word1.lower()
    word2Lower = word2.lower()
    word1_count_dict = count_letters(wordLower)
    word2_count_dict = count_letters(word2Lower)

    if word1_count_dict == word2_count_dict:
      return True
    else:
      return False


def checkAnagram(word1, word2):
    wordLower = word1.lower()
    word2Lower = word2.lower()
    word1_count_dict = count_letters(wordLower)
    word2_count_dict = count_letters(word2Lower)

    if len(word1_count_dict) != len(word2_count_dict):
        return False

    for key in word1_count_dict:
        if key not in word2_count_dict:
            return False
        if word1_count_dict[key] != word2_count_dict[key]:
            return False

    for key in word2_count_dict:
        if key not in word1_count_dict:
            return False
        if word1_count_dict[key] != word2_count_dict[key]:
            return False

    return True


if checkAnagram("aNaGrAm", "NaGaRaM"):
    print("These words are anagrams!")
else:
    print("These words aren't anagrams!")