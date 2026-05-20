#Arithmetic and Math

Friends = 15
Friends = Friends + 1
print (Friends)

Friends = 15
Friends += 1
print (Friends)

Friends = 15
Friends = Friends -2
print (Friends)

Friends = 15
Friends  -=2
print (Friends)

Friends = 15
Friends = Friends * 3
print (Friends)

Friends = 15
Friends = Friends / 2
print (Friends)

Friends = 15
Friends /= 2
print (Friends)

x =3.14
y =-4
z = 5

result = abs(y)
print(result)
result = round (x)
print(result)
result = pow(4,3)
print(result)
result = max(x,y,z)
print(result)
result = min(x,y,z)
print(result)

import math
print (math.pi)
print (math.e)
x = 9
result = math.sqrt(x)
print(result)
y=9.1
result = math.ceil(y)
print(result)
z=9.9
result = math.floor(z)
print(result)

import math
radius = float(input ("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}")

import math 
radius = float(input ("Enter the radius of the circle: "))
area = math.pi * radius * radius
print(f"The are of the circle is: {round(area,2)}")

import math 
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a,2)+ pow(b,2))
print(f"The Side C = {c}")