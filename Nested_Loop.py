# # Nested Loop = loop within another loop (Outer, inner)
# # outer loop:
# #   inner loop:

# # Can have while loop inside a while loop
# # Can have for loop inside the for loop
# # Can have while loop inside for loop
# # Can have for loop inside a while loop
# for x in range (1,10):
#     # print(x,end="")
#     # print(x,end=" ")
#     print(x,end="-")


# for x in range(3):
#     for y in range (1,10):
#         print(y,end="")
#     print()

rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of columns:"))
Symbol = input("Enter the Symbol :")

for x in range(rows):
    for y in range (cols):
        print(Symbol,end="")
    print()