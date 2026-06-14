# Dictionary = a collection of {key : value} pairs
#           ordered and changeable. No Duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}

#different attributes and methods of a dictionaries
print(dir(capitals)) 

# How to use it we use the help function
print(help(capitals)) 

# # few methods
# print(capitals.get("India"))
# print(capitals.get("Japan"))

# # using a if statment

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital does not exist")

# # to update a dictionary
# print(capitals)
# capitals.update({"Germany": "Berlin"}) #adding
# capitals.update({"USA":"Detroit"}) #updating the already existin one  

# #to remove the key
# capitals.pop("China") 

# #it will remove the latest key added to the dictionary
# capitals.popitem() 

# #it will clear the dictionary
# capitals.clear() 
# print(capitals)

# # to get the keys in the dictionary
# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# #to get the value in the dictionary
# values = capitals.values()
# print(values)
# for value in capitals.values():
#     print(value)

# #ITEMS METHOD
# items = capitals.items() # items returns a 2D list of tuples and items =[(),(),()]
# print(items)
# for key, value in capitals.items():
#     print(f"{key}:{value}")