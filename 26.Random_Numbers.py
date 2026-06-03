import random

# print(help(random))

low = 1
high = 100

# number = random.randint(1,20)
# number = random.randint(low,high)

number = random.random() #Random floating point number between 0 and 1
print(number)

options = ("rock", "paper", "scissors") #Using a tuple
option = random.choice(options)
print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #LIST
random.shuffle(cards)
print(cards)