# Countdown timeer 

import time

time.sleep(3)
print("Time's up")

my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)
print("Time's Up!")


# to print in reverse
for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)
print("Time's Up!")

# another technique to print in reverse function
for x in range(my_time,0, -1):
    print(x)
    time.sleep(1)
print("Time's Up!")

# To add seconds,minutes ,hours
for x in range(my_time,0, -1):
    seconds = x % 60
    minutes = int (x/ 60) % 60
    hours = int (x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's Up!")