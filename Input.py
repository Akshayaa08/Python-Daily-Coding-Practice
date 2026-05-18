#Input()
# A Function that prompts the user to enter daa 
# Returns the entered data as a string

name = input("Enter your name:")
age =input("Enter your age:")
#the age is collected as a string, we need to convert it to an integer to perform arithmetic operations on it.
age =int(age)
age = age+1
age =int(input("Enter your age:"))
print(f"Hello {name}, you are {age} years old")

#Exercise : Rectangle Area Calculator
Length = int(input("Enter the length of the rectangle:"))
Width = int(input("Enter the width of the rectangle:"))
area = int(Length)*int(Width)
print (area)
