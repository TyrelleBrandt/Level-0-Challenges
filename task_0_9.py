def vowels_in_a_word(word):
    vowels = "AEIOUaeiou"
    list1 = word.lower()
    list2 = []
    for x in list1:
        if x.lower() in vowels:
            if x in vowels:
                list2.append(x)
    vowes = list(dict.fromkeys(list2))
    final_vowels = ", ".join(vowes)
    return "Vowels: " + final_vowels


print(vowels_in_a_word("Umuzi"))
