import math

def function (a,b,c):
    theta = math.acos((a**2 + b**2 - c**2)/a*b)
    area = 0.5* a*b*math.sin(theta)
    return area
    
