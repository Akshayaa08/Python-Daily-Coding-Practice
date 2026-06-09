# default arguments = a default value for certain paramters
# default is used when that argument is omitted
# make your funvtions more flexible, reduces # of arguments
# 1. positional, 2.Default, 3. Keyword 4.Arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price *(1-discount)*(1+tax)
print(net_price(500))
# Even whhen default arguments are set arguments are passeed it takes those into consideration
print(net_price(500,0.2,0)) 

# import time

# def count(start,end):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")

# print(count(1,3))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

print(count(10))