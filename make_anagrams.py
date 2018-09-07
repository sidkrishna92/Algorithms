def makeAnagram(a, b):
    dict = {}
    count = 0

    for letter in a:
        if letter not in dict:
            dict[letter] = 0
        dict[letter] += 1

    for letter in b:
        if letter not in dict:
            dict[letter] = 0
        dict[letter] -= 1

    count = sum(abs(n) for n in dict.values())
    return count

str_1 = 'bdce'
str_2 = 'arbsfr'
print(makeAnagram(str_1, str_2))