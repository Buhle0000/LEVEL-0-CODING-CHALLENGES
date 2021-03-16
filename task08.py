number = float()
def convert(number):
    hours = int(number // 60)
    return hours

hours = convert(number)
minutes = int(number % 60)
if hours <= 1 and minutes > 1:
    print(f"{hours} hour and {minutes} minutes ")
elif hours > 1 and minutes <= 1:
    print(f" {hours} hours and {minutes} minute")
else:
    print(f"{hours} hours and {minutes} minutes ")
