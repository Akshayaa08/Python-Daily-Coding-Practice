# Problem Scenario
# income tax - 50000
# income tax ku 20% tax and calculate and show
# for all 5annual income 
# 0-10000 - 0%
# 10000 -50000 -10%
# above 50000 - 20%



salary = int(input("Enter your salary: "))
tax = 0

if salary> 10000 and salary < 50000:
    tax = salary*0.1
    print(f"Tax deducted for the {salary} is : {tax}") 
               
elif salary >50000:
    new_salary = salary - 50000
    if new_salary> 10000 and new_salary<50000:
        ns1 = new_salary - 10000
        tax = ns1*0.1+ 50000*0.2
        print(f"Tax deducted for the {salary} is : {tax}") 

    else:
        tax = 50000*0.2 + new_salary
        print(f"Tax deducted for the {salary} is : {tax}") 

else:
   print(f"No tax is deducted for {salary}" )


# def calculate_tax(income):
#     tax = 0
#     if income<10000:
#         return
    
#     if income 

salary = int(input("Enter your salary: "))
tax = 0

if salary <= 10000:
    tax = 0

elif salary <= 50000:
    tax = (salary - 10000) * 0.10

else:
    tax = (50000 - 10000) * 0.10 + (salary - 50000) * 0.20

print(f"Tax deducted for {salary} is: {tax}")