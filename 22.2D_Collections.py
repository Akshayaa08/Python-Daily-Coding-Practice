# 2D Collection

fruits    = ["apple","banana","orange","pineapple"]
vegetable = ["carrot","brinjal","tomato"]
meat      = ["fish","chicken","mutton"]

groceries = [fruits,vegetable,meat]

print(groceries)
print(groceries[0])
print(groceries[0][0])

groceries = [["apple","banana","orange","pineapple"],
             ["carrot","brinjal","tomato"],
             ["fish","chicken","mutton"]]
print(groceries)
print(groceries[0])
print(groceries[0][1])


for collection in groceries:
    for food in collection:
        print(food, end =" ")
    print()


num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for rows in num_pad:
    for num in rows:
        print(num, end=" ")
    print()

