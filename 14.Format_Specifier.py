# format specifier ={value:flags} format a value based in what flags are inserted

# .(number) f = round to that many decimaml places(fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a pls sign to indicate positive value
# := = place sign to leftmost position
#    = insert a space before positive numbers
# ,  = comma separator


price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# .(number) f = round to that many decimaml places(fixed point)
print(f"Price 1 : {price1: .2f}")
print(f"Price 2 : {price2: .2f}")
print(f"Price 3 : {price3: .2f}")

# :(number) = allocate that many spaces
print(f"Price 1 : {price1:10}")
print(f"Price 2 : {price2:10}")
print(f"Price 3 : {price3:10}")

# :03 = allocate and zero pad that many spaces
print(f"Price 1 : {price1:010}")
print(f"Price 2 : {price2:010}")
print(f"Price 3 : {price3:010}")

# :< = left justify
print(f"Price 1 : {price1:<10}")
print(f"Price 2 : {price2:<10}")
print(f"Price 3 : {price3:<10}")

# # :> = right justify
print(f"Price 1 : {price1:>10}")
print(f"Price 2 : {price2:>10}")
print(f"Price 3 : {price3:>10}")

# # :^ = center align
print(f"Price 1 : {price1:^10}")
print(f"Price 2 : {price2:^10}")
print(f"Price 3 : {price3:^10}")

# :+ = use a pls sign to indicate positive value
print(f"Price 1 : {price1:+}")
print(f"Price 2 : {price2:+}")
print(f"Price 3 : {price3:+}")

# := = place sign to leftmost position
print(f"Price 1 : {price1:=10}")
print(f"Price 2 : {price2:=10}")
print(f"Price 3 : {price3:=10}")

#    = insert a space before positive numbers
print(f"Price 1 : {price1: }")
print(f"Price 2 : {price2: }")
print(f"Price 3 : {price3: }")

# ,  = comma separator (Each thousand's place separated by a comma)
print(f"Price 1 : {price1:,}")
print(f"Price 2 : {price2:,}")
print(f"Price 3 : {price3:,}")

# can combine the format spcifier

print(f"Price 1 : {price1:+,.2f}")
print(f"Price 2 : {price2:+,.2f}")
print(f"Price 3 : {price3:+,.2f}")