from decimal import Decimal

PIE  = 3.141592653589793238462643
radius = float(input("Enter radius of circle: "))

circumference_of_a_circle = 2 * PIE * radius
diameter_of_a_circle = circumference_of_a_circle // PIE
area_of_circle = PIE * radius**2


print(f'Diameter of circle = {round(diameter_of_a_circle,2)} units')
print(f'Circumference of circle = {round(circumference_of_a_circle,2)} units')
print(f'Area of circle = {round(area_of_circle,2)} sq units')



