# collection = single "variable" used to store multiple values
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable. but add/ remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# ************************* LIST ******************************
fruits = ["apple","orange","banana","coconut"]
print(fruits)
print(fruits[0])
print(fruits[0:2])
print(fruits[::2]) # to skip after 2
print(fruits[::-1]) # to reverse

for x in fruits:
    print(x)

 # to list the different function availabe 
print(dir(fruits))

# for description of each function
print(help(fruits)) 

# to print the length of the collection
print(len(fruits))  

#boolean function
print("apple" in fruits)
print("pineapple" in fruits)

# in list we can change
fruits[0]="pineapple"
print(fruits)

#to append
fruits.append("pineapple")
print(fruits)

#to remove
fruits.remove("orange")
print(fruits)
 
# to insert
fruits.insert(0,"pineapple")
print(fruits)

# to sort
fruits.sort()
print(fruits)

# to reverse
fruits.reverse()
print(fruits)

# to clear
fruits.clear()
print(fruits)

# to return the index of a value
print(fruits.index("apple"))

# to count
print(fruits.count("banana"))


# **************************** SET *******************************
fruits ={"apple","orange","banana","coconut","coconut "}
print(fruits) #no duplicates

 # to list the different function availabe 
print(dir(fruits))

# for description of each function
print(help(fruits)) 

# to print the length of the collection
print(len(fruits))  

#boolean function
print("apple" in fruits)
print("pineapple" in fruits)

# INDEXING OF THE SET IS NOT AVAILABE AS IT IS UNAVAILABE
print(fruits[0]) # it gives error

#add element
fruits.add("pineapple")
print(fruits)

# to remove
fruits.remove("apple")
print(fruits)

# to pop method
# the pop method removes the first element whatever elements is present at first
fruits.pop()
print(fruits)

# to clear
fruits.clear()
print(fruits)


# **************************** TUPLE *******************************
fruits =("apple","orange","banana","coconut","coconut")
print(fruits)

 # to list the different function availabe 
print(dir(fruits))

# for description of each function
print(help(fruits)) 

# to print the length of the collection
print(len(fruits))  

#boolean function
print("apple" in fruits)
print("pineapple" in fruits)

# Indexing
print(fruits.index("apple"))

# count
print(fruits.count("coconut"))

# iterable
for fruit in fruits:
    print(fruit)