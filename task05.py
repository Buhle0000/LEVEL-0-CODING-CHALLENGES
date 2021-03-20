def area_of_triangle(a,b,c):

    semi = (a + b + c)/2
    area = str((semi * (semi - a) * (semi - b) * (semi - c))**0.5)
    print(f"Area of Triangle is {area}")
   
area_of_triangle(6,5,5)   
    
