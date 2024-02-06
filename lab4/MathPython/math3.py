import math

def area_polygon(n, s):
    area = (n*s**2)/4*math.tan(math.pi/n)
    return area

print(math.ceil((area_polygon(4, 25))))