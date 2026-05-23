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

#Exercise 1 : Rectangle Area Calculator
Length = int(input("Enter the length of the rectangle:"))
Width = int(input("Enter the width of the rectangle:"))
area = int(Length)*int(Width)
print (area)


#Exercise 2 : Shopping  Cart Program
item = input ("Enter the item you want to buy:")
price = float(input("Enter the price of the items:"))
quantity = int(input("Enter the quantity of the items:"))
total = price * quantity
print(f"Total cost for {quantity} {item}(s): ${total:.2f}")

