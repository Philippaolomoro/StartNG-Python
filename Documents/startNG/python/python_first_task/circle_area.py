import math

def circle_area(radius):
    return math.pi * (radius ** 2)

rad = float(input("Enter a radius: "))
print(circle_area(rad))