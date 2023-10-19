
import math



def square_foot(length, width):
    return length + width

length_of_house =float( input('Enter the length of the house in feet: '))

width_of_house =float( input('Enter the width of the house in feet: '))

house_sqft= square_foot(length_of_house, width_of_house)
print(f'The square footage of the house is {house_sqft:.2f} square feet.')




def circum_circle(radius):
    return 2* math.pi * radius

radius_of_circle= float(input('Enter the radius of the circle in feet: '))
circumferencce_of_circle =circum_circle(radius_of_circle)
print(f' The circles circumference equals {circum_circle:.2f} feet.')