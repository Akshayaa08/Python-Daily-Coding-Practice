# Function = A block of reuseable code
# place () after the function name to invoke it


# to define a function
def happy_birthday():
    print("Happy Birthday to you!")
    print("You are old")
    print("Happy Birthday to you!")
    print()
# to call a function to invoke it
happy_birthday()

# Function with a parameter
def happy_birthday(name,age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age}")
    print("Happy Birthday to you!")
    print()
happy_birthday("Bro",20)
happy_birthday("Gino",24)
happy_birthday("Akshayaa",23)

# to display bills
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your payment amount is {amount:.2f}")
    print(f"Your due date is :{due_date}")

display_invoice("Aksh", 1234.456,"01.01.2027" )


# return = statement used to end a function 
# and send a result back to the caller

def add(x,y):
    z = x+y
    return z

def sub(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z =x/y
    return z

print(add(1,3))
print(sub(5,2))
print(multiply(10,2))
print(divide(20,4))

# Create a function to create a name

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first+" "+last

full_name = create_name("gino","singh")
print(full_name)