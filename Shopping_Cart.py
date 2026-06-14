# Shopping Cart exercise

foods =[]
prices = [] #list ordered and changeable
total = 0

while True:
    food=input("Enter the food (q to quit): ")
    if foods.lower=="q":
        break
    else:
        price = float(input(f"Enter the price of a food {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART------")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total amount is {total}")