celsius = float(input("What's the temperature(c)? :"))
def convert(celsius):
    fahrenheit = 32 + (celsius * 9/5)
    return fahrenheit

fahrenheit = convert(celsius)
print(f"Temperature in fahrenheit is {fahrenheit}")

