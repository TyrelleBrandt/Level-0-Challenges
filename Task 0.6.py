a = 10
d = 33
b = 20
c = 25

def maximum(a, d, b, c):
    if (a >= b) and (a >= c) and (a >= d):
        largest = a
    elif (b >= a) and (b >= c) and (b >= d):
        largest = b
    elif (c >= a) and (c >= b) and (c >= d):
        largest = c
    else:
        largest = d
    return largest
print(maximum(a, d, b, c))