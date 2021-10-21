str1 = "house"
str2 = "computers"

result = []
if (len(str1) < len(str2)):
    for a in str1:
        if(a in str2):
            result.append(a)
else:
    for a in str2:
        if(a in str1):
            result.append(a)
print('Common letters:', *result)
