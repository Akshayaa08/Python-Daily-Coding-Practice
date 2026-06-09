# Python Dictionary Problems:
# 1. d = {"a": 1, "b": 2, "c": 3}count the number of keys in a dictionary.
# 2.Write a Python program to iterate over dictionaries using for loops.
# 3.Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# solve these prbmls if u have completed dictonary.
 
#Solution for Problem 1
d = {"a": 1, "b": 2, "c": 3}
total=0
for key in d.keys():
    total+=1
print(total)

#Solution for Problem 2
d = {"a": 1, "b": 2, "c": 3}
for key,value in d.items():
    print(f"{key}:{value}")

#Solution for Problem 3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)