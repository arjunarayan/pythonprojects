def capitalize(sentence):
    words = sentence.split(" ")
    changed_words = []
    for word in words:
        first = word[0].upper()
        rest = word[1:].lower()

        changed_words.append(first+rest)
    new_sentence = ' '.join(changed_words)
    return new_sentence

print(capitalize("PYTHON is AwEsoMe RiGhT"))
