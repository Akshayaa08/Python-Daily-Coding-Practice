#For Loops = execute a block of code a fixed number of times
# You can iterate over a range, strings, sequence, etc

# to count a 10 times 
for x in range (1,11):  # it begins at 1 and ends at 11 
    print(x)            # the output is 1,2,3,4,5,6,7,8,9,10

# to reverse a function
for x in reversed (range(1,11)):
    print(x)
print("Happy New Year!")

# to count a number in a step function 
for x in range (1,11,3): 
    print(x)           

# To print the credit card number
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

# to skip over the iteration or skip a number

for x in range (1,21):
    if x ==13:
        continue
    else:
        print(x)

# To break a function 

for x in range (1,21):
    if x ==13:
        break
    else:
        print(x)