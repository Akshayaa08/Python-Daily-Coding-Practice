# Python calculator 

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# num1 = input("Enter the 1st number: ") 10
# num2 = input("Enter the 2nd number: ") 11
# print(num1 + num2)  1011 - the input is taken as a string and the output is string concatenated

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} is not a valid operator")