# # *args (arguments) = allows you to pass multiple non-key arguments
# **kwargs(keyword arguments) = allows you to pass mutliple keyyword-arguments
# * unpacking operator
# 1. positional, 2.default, 3.Keyword , 4. Arbitrary


#----------------------------*args--------------------------------
# *ARGS ARE A TUPLE
def add(a,b):
    return a+b
print(add(1,2))
# but what if i place 3 arguments i shows an error

# def add(*args):
def add(*nums):
    total=0
    for num in nums:
        total+=num
    return total

print(add(1,2,3,4))

def display_names(*args):
    for arg in args:
        print(arg, end=" ")

(display_names("Gino","Singh","Akshayaa"))

# ----------------------------------**kwargs----------------------------------
# **KWARGS ARE DICTIONARY
def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_address(street ="123 fake street",
              city="Detroit",
              state ="MI",
              zip="54321")

# Exercise in combing both args and kwargs
#KWARGS MUST FOLLOW THE POSITIONAL ARGUMENT
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
      
shipping_label("Dr.","Spongebob","Squarepants","III",
              street ="123 fake street",
              city="Detroit",
              state ="MI",
              zip="54321")