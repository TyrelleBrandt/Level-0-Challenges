def fahrenheit_to_celsius(temp1):
    celsius = (temp1 - 32) * 5 / 9
    return celsius


print(fahrenheit_to_celsius(85))


def celsius_to_fahrenheit(temp2):
    fahrenheit = (temp2 * 9 / 5) + 32
    return fahrenheit


print(celsius_to_fahrenheit(25))
