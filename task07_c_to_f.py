celsius = float()
def convert(celsius):
    fahrenheit = 32 + (celsius * 9/5)
    return fahrenheit

fahrenheit = convert(celsius)
print(f"Temperature in fahrenheit is {fahrenheit}")

