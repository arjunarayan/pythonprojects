"""
Case 1:
    Input: "abba", "dog cat cat dog"
    Output: True

Case 2:
    Input: "abba", "dog cat cat fish"
    Output: False

Case 3:
    Input: "aaaa", "dog cat cat dog"
    Output: False

"""

def checkPattern(pattern: str, s:str) -> bool:
    patternDict = {}
    sDict = {}
    s = s.split(" ")
    if len(pattern) != len(s):
        return False
    else:
        for i in range(0, len(pattern)):
            if pattern[i] not in patternDict and s[i] not in sDict:
                patternDict[pattern[i]] = s[i]
                sDict[s[i]] = pattern[i]
            else:
                if pattern[i] in patternDict and patternDict[pattern[i]] != s[i]:
                    return False
                if s[i] in sDict and sDict[s[i]] != pattern[i]:
                    return False
    return True

print(checkPattern("dadd", "bruh pizza bruh bruh"))