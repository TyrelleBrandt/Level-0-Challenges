def areatriangle_function(a, b, c):
    s = int(a + b + c) / 2
    return (s * (s-a) * (s-b)* (s-c)) ** 0.5

print(areatriangle_function(4, 6, 8))
