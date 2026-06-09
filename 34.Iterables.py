# iterable = an object/collection that can return its elements one at a  time,
# allowing it to be iterated over in a loop

#LIST
numbers = [1,2,3,4,5]
for number in numbers:
    print(number, end=" ")
print()
for number in reversed(numbers):
    print(number, end=" ")
print()
#SET
print()
fruits ={"apple","orange","banana","coconut"}
for fruit in fruits:
    print(fruit)
#STRING
print()
name ="Gino Singh"
for character in name:
    print(character, end="")

#DICTIONARY
print()
my_dictionary={"A":1,"B":2,"C":3}
print()
for value in my_dictionary.values():
    print(value)
print()
for key in my_dictionary.keys():
    print(key)
print()
for key,value in my_dictionary.items():
    print(f"{key}:{value}")
print()