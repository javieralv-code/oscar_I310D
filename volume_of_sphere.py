import math
def calculate_volume_of_sphere(r):
    pi = math.pi
    volume = (4/3) * pi * r ** 3
    return volume

radius1 = 5
volume1 = calculate_volume_of_sphere(radius1)
print(f"The volume of a sphere with radius {radius1} is: {volume1}")

radius2 = 10
volume2 = calculate_volume_of_sphere(radius2)
print(f"The volume of a sphere with radius {radius2} is: {volume2}")
