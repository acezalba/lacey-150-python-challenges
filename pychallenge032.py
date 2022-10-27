import math

radius = float(input("Enter the cylinder radius: "))
depth = float(input("Enter the cylinder depth: "))
print(round(depth * math.pi * (radius**2), 3))
