def remove_vowels_it(s):
    if len(s) >= 1:
        if s[0] in "aeiouy":
            return remove_vowels_it(s[1:])
        else:
            return s[0] + str(remove_vowels_it(s[1:]))
    else:
        return s


word = input("Entrez un mot")
result = remove_vowels_it(word)
print(result)
