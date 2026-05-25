# # Python compound interest calculator

# #declaring
# principle = 0
# rate = 0
# time = 0


# while principle <=0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <=0:
#         print("Principle can't be less than or equal to zero")

# while rate <=0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <=0:
#         print("Interest rate can't be less than or equal to zero")

# while time <=0:
#     time = float(input("Enter the time in years: "))
#     if time <=0:
#         print("Time can't be less than or equal to zero")

# # print(principle)
# # print(rate)
# # print(time)

# total = principle * pow((1 + rate/100), time)
# print(f"The amount after {time}years : ${total:.2f}")



#Another way is to keep the running the program
while True:
    principle = float(input("Enter the principle amount: "))
    if principle <0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <0:
        print("Time can't be less than or equal to zero")
    else:
        break

# print(principle)
# print(rate)
# print(time)

total = principle * pow((1 + rate/100), time)
print(f"The amount after {time}years : ${total:.2f}")