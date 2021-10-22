a = 4
b = 6                
c = 8
s = int(a + b + c) / 2

def areatriangle_function():
    return (s * (s-a) * (s-b)* (s-c)) ** 0.5

print(areatriangle_function())
