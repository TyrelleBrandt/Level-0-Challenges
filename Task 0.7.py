temp1 = 85
temp2 = 25

def fahrenheit_to_celsius(temp1):
    celsius = (temp1 - 32) * 5/9
    print(celsius)
fahrenheit_to_celsius(temp1)

def celsius_to_fahrenheit(temp2):
    fahrenheit = (temp2 * 9/5) + 32
    print(fahrenheit)
celsius_to_fahrenheit(temp2)
