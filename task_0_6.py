def maximum_number(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    elif (c >= a) and (c >= b):
        largest = c
    return largest


print(maximum_number(10, 20, 25))