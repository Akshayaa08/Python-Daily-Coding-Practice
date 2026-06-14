# Modules = a file containing code you want to include in your program
# use 'import' to include a module (built in or your own)
# useful to break up a large program resuable separate files

# print(help("modules"))
 
# import math
import math as m
print(m.pi)

from math import pi
print(pi)

print()
from math import e
print(e)
a,b,c,d=1,2,3,4
print(math.e**a)
print(math.e**b)
print(math.e**c)
print(math.e**d)
# I have declared from e and it doesnt use the e from the math module
a,b,c,d,e=1,2,3,4,5 
print(e**a)
print(e**b)
print(e**c)
print(e**d)
print(e**e)

#To creating a individual file and importing
import example
result = example.pi
print(result)
result = example.square(3)
print(result)
result = example.cube(3)
print(result)
result = example.circumference(3)
print(result)
result = example.square(3)
print(result)
