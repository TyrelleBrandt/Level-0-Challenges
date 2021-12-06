def area_triangle_function(a, b, c):
    s = int(a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


print(area_triangle_function(4, 6, 8))
