# String Methods


name = input("Enter your full name: ")
String_Length
result = len(name)
print(result)

#to find any character in a string
res=name.find(" ")
print(res)

#to find the last occurence of 
res1 = name.rfind("a")
print(res1)

#to capitalize the first letter of a string
name=name.capitalize()
print(name)

#to capitalize all the letters in a string
name1 = name.upper()
print(name1)    

# to lower all the characters in a string
low = name.lower()
print(low)

# to check whether the given is ALL digits
res3= name.isdigit()
print(res3)

# to check all the characters are alphabets
# IF SPACE ARE PRESENT IN BETWEEN IT WILL RETURN FALSE
res4 = name.isalpha()
print(res4)

phn_num = input("Enter the phone number: ")
result = phn_num.count("-")
print(result)

result1 = phn_num.replace("-"," ")
print(result1)

print(help(str))

# EXERCISE
# VALIDATE USER INPUT EXERCISE
# 1.Username is no more than 12 Characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username has more than 12 characters")
elif not username.find(" ")== -1:
    print("Your username has a space ")
elif not username.isalpha():
    print("Your username has digits")
else:
    print(f"Welcome {username}") 
