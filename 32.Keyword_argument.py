#Keyword Arguments = an argument preceded by an identifier
# helps with readbility
# order of arguments doesn't matter
# 1. positional, 2.default, 3.Keyword , 4. Arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}.{first} {last}")
hello("hello", title="Mr", first="Gino", last="Singh")
# positiional arguments follows the keyword arguments

#End keyword Argument
for x in range(1,11):
    print(x, end=" ")

#separate keyword argument
print("1","2","3","4","5",sep="-")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1, area=34, first=1234, last=98765)
print(phone_num)