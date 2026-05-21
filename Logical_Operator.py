# logical operators = evaluate multiplel condition (or, and, not)
# or = at least one condition must be true
# and = both conditions must be true
# not =  invests the condition (not false, not true)


# Logical Operator - OR
temp = 20
is_raining = True

if temp>= 28 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# Logical Operator - AND

temp = -5
is_sunny = True
if temp>= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD outide")
    print("It is CLOUDY")