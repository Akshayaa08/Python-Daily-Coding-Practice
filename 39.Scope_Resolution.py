# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in 

# # Basic Functions
def func1():
    a = 1
    print(a)
#the variables in a cannot be accessed in func1
def func2():
    b = 2
    print(b)
#the variables in a cannot be accessed in func2
func1()
func2()

# # Local scope resolution Functions
def func1():
    x = 1
    print(x)
def func2():
    x = 2
    print(x)
func1()
func2()

# #Enclosed Scope resolution function
# # Enclosed scope function 1
def func1():
    x = 1
    def func2():
        x = 2
        print(x)
    func2()
func1()

# #Enclosed scope function 2
#  #If x is not present in the local scope we would find x in the enclosed scope 
def func1():
    x = 1
    def func2():
         print(x)
    func2()
func1()


# #Global Scope Resolution
def func1():
    print(x)
def func2():
    print(x)
x=3
func1()
func2()

# # Built-in Scope Resolution
from math import e

def func1():
    print(e)

func1()

from math import e

def func1():
    print(e)
e=3 # i am using a global scope so in order it will print the global scope than the built-in scope
func1()