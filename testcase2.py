def alternatingCharacters(s):
    d = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            d += 1
    return d

def test_alternatingCharacters():
    assert alternatingCharacters("") == 0
    assert alternatingCharacters("A") == 0
    assert alternatingCharacters("AAAA") == 3
    assert alternatingCharacters("BBBBB") == 4
    assert alternatingCharacters("ABABAB") == 0
    assert alternatingCharacters("AABBB") == 3
    assert alternatingCharacters("XYXYXY") == 0
    assert alternatingCharacters("XXYYZZ") == 3 
    assert alternatingCharacters("M" * 1000) == 999
    assert alternatingCharacters("AB" * 500) == 0
    assert alternatingCharacters("AABBAABB") == 4
    assert alternatingCharacters("ABCDE") == 0
    assert alternatingCharacters("AAABBB") == 4 

test_alternatingCharacters()
print("All passed ✅")
