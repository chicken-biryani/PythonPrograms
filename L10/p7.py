#wapp to read radius from the user find area & circumference using math module

import math
radius = float(input("Enter radius "))
area = math.pi * math.pow(radius, 2)
circum = 2 * math.pi *radius
print("Area = %.2f " %area)
print("Circumference = %.3f" %circum)
print("Area = %.2f Circumferemce = %.3f" %(area,circum))