import math

def maximum(a,b,c):
    maxi = 0
    if( a > b and b > c):
        maxi = a
    elif( b > c and c > a):
        maxi = b
    else:
        maxi = c
    return maxi    

