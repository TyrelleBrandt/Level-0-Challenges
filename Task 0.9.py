vowels = ('aeiou')

word = str.lower(input())

def vowelsinword():
    list1 = list(word)
    list2 = []
    for x in list1:
        if x.lower() in vowels:
            if x in vowels:
             list2.append(x)
    vowes = ', '.join(list2)

    print("Vowels: "+ vowes)
vowelsinword()
