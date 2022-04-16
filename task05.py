def area_of_triangle(side1, side2, side3):
    semi_perimeter = (side1 + side2 +side3) * 0.5
    area = str((semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5)
    return area
    
