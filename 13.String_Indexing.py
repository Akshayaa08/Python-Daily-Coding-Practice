#indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_number ="1234-5678-9012-3456"

print(credit_number[0])             # to fetch one character
print(credit_number[:5])            # to fetch from starting to the end
print(credit_number[4:9])           # to fecth character between the range
print(credit_number[5:])            # to fetch characters from starting to the end 
print(credit_number[-1])            # to fetch characters in reverse order
print(credit_number[::3])           # to fetch every characters in a step conditions
print(credit_number[-4:])           # to fetch data from alternative way, the output is : 3456

last_digits =credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# to reverse a character in a string

credit_number = credit_number[::-1] # to reverse a string you need to use -1 in step
print(credit_number)