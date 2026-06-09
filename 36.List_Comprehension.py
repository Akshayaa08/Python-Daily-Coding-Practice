#List_Comprehension = A concise way  to create list in python
# compact and easier to read than traditional loops
# [expression for value in iterables if condition]

doubles = [ x*2 for x in range(1,11)]
print(doubles)
triples = [y*3 for y in range(1,11)]
print(triples)
squares = [z*z for z in range(1,11)]
print(squares)

print()

fruits =["apple","orange","banana","coconut"]
fruits= [fruit.upper() for fruit in fruits]
print(fruits)

fruits =["apple","orange","banana","coconut"]
fruit_chars= [fruit[0] for fruit in fruits]
print(fruit_chars)

print()

numbers = [1,-2,3,-4,5,-6,8,-8,7]
positive_nums = [num for num in numbers if num>=0]
print(positive_nums)
negative_nums = [num for num in numbers if num<=0]
print(negative_nums)
even_nums=[num for num in numbers if num % 2==0]
print(even_nums)
odd_nums=[num for num in numbers if num %2 ==1]
print(odd_nums)

print()

grades = [85,42,79,90,56,61,30]
passing_grades =[grade for grade in grades if grade>=60 ]
print(passing_grades)