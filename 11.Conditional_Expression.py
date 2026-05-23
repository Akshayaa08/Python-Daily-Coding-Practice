# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition 
# X if condition else Y

num = 6

print("Positive" if num > 0 else "Negative")
print("Even" if num %2==0 else "Odd")

a=8
b=5
print("a" if a>b else "b")
print("a" if a<b else "b")

age =23
print("Adult" if age>=18 else "Child")

temp = 30  
print("Hot" if temp else "Cold")

user_role ="Admin"
print("Full Access" if user_role=="Admin" else "Denied")