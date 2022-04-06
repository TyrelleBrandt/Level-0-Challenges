def area_of_a_triangle(side_a, side_b, side_c):
    semi_perimeter = (side_a + side_b + side_c) / 2
    return (semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)) ** 0.5


print(area_of_a_triangle(4, 6, 8))
