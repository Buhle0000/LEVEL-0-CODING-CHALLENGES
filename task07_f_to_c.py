fahrenheit = float()
def convert(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = convert(fahrenheit)
print(f"temperature in celsius is {celsius}")

