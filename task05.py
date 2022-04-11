def area_of_triangle(a, b, c):
    semi_perimeter = (a + b +c) * 0.5
    area = str((semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5)
    return area
    
