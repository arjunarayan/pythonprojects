string = "Hello Hello world from space space I'm going to Elio movie movie later and it is suuuuper awesome"
string_split = string.split(" ")
word_dict = {}
for word in string_split:
    lowercase_word = word.lower()
    if lowercase_word in word_dict:
        word_dict[lowercase_word] += 1
    else:
        word_dict[lowercase_word] = 1
print(word_dict)