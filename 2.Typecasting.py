#Typecasting
#Typecasting is the process of converting a variables from one datatype to another datatype

name ="Akshayaa"
age = 25 
gpa = 8.5
is_student =True

print(type(name)) #str
print(type(age)) #int
print(type(gpa)) #float
print(type(is_student)) #bool

#Conversion of the datatype of the variable
gpa = int(gpa)
print(gpa)
age = str(age)
print(age)
print(type(age)) #int
age +="1"
print(age)
name = bool(name)
print(name)
