vowels = ['a', 'e', 'i', 'o', 'u']

word = str.lower("Umuzi")

list1 = list(word)
list2 = []
for x in list1:
    if x.lower() in vowels:
        list2.append(x)
vowes = ', '.join(list2)
print("Vowels: "+vowes)
