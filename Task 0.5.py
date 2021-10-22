a = 4                   # a is the 1st side of a triangle.
b = 6                   # b is the 2nd side of a triangle.
c = 8                   # c is the 3rd side of a triangle.
s = (a + b + c) / 2

def my_function():
    return (s * (s-a) * (s-b)* (s-c)) ** 0.5

print(my_function())
