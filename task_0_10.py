def common_letters(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    result = []
    if len(str1) < len(str2):
        for a in str1:
            if a in str2:
                result.append(a)
    else:
        for a in str2:
            if a in str1:
                result.append(a)
    result = list(set(result))
    final_letters = ",".join(result)
    print("Common letters:", *final_letters)


common_letters("technology", "computers")
