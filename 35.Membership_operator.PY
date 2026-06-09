# Membership operator = used to test whether a value or valuable is found in a sequence
# (string, list, tuple, set or dictionary)
# 1. in
# 2. not in

# #In a string
# word = "APPLE"
# letter = input("Guess a letter in the secret word: ").upper()
# # in
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")
# # not in
# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

# # Set
# students = {"Spongebob","Patrick", "Sandy"}
# student = input("Enter the name of student: ")

# if student in students:
#     print(f"{student} is present in students")
# else:
#     print(f"{student} is not present")

# # Dictionary
# grades = {"Sandy": "A","Squidward":"B"}
# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# exercise
email="BroCode@gmailcom"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")