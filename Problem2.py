# Problem 2

# Employee payroll calculation
# basic salary - user input
# employee name, basic salary, city type - metro/urban/tier1 and designation from particular employee other from user
# HRA - 24% OR OTHER 18%
# Logic - to calculate the house rent based on the city type for metro 24%, tier1 - 18% and other is 12%. 
# PF 12% Of basic salary and 10% for income tax for GROSS SALARY.
# Con allowance - 10,000 for manager and other designation IS DEVELOPER AND OTHER their allowance is 5,000.
# Special Allowance or DA is the 12% of the basic salary 

# GROSS SALARY = Basic salary +HRA+ SPEACILA ALLOWANCE + CON ALLOWANCE

# 50000 = BASIC SALARY
# HOUSE RENT = 25%
# DA = Fixed 
# con allowance = manager or developer
# sum of all these or gross salary 

# then go for the deduction 
# PF 
# Income tax = gross salary * 10%
# finally is your net salary

# output
# emp name
# emp basic salary
# hra
# da
# gross salary
# pf deduction
# net take 

print("---------------------------------------------------------------------------")
print("Employement Payroll Calculation")
emp_name = input("Enter your name: ")
basic_sal = int(input("Ente your Basic Salary: "))
ciy__type = input("Enter the city type (metro/tier1/others): ")
designation = input("Enter your designation : ")

if ciy__type.lower() == "metro":
    hra = basic_sal*0.24
elif ciy__type.lower() =="tier1":
    hra = basic_sal*0.18
else:
    hra = basic_sal*0.12

da = basic_sal*0.12

if designation.lower() =="senior manager" or designation.lower()== "manager":
    convenient_allowance = 10000
else:
    convenient_allowance = 5000

gross_salary = basic_sal + hra + da + convenient_allowance

#deduction

pf = basic_sal * 0.12
income_tax = gross_salary * 0.10 #0.10
total_deduction = pf+income_tax
net_sal = gross_salary - total_deduction
# con_allowance print, variables name change
print(f"Employee name: {emp_name}")
print(f"Basic salary of a employee: ₹{basic_sal:.2f}")
print(f"HRA :₹{hra:.2f}")
print(f"DA or Special Allowance: ₹{da:.2f}")
print(f"Convenient Allowance: ₹{convenient_allowance:.2f}")
print(f"Gross salary of a employee: ₹{gross_salary:.2f}")
print(f"PF of the employee: ₹{pf:.2f}")
print(f"Income tax of the employee: ₹{income_tax:.2f}")
print(f"Net Salary : ₹{net_sal}")
print("---------------------------------------------------------------------------")


# Using Functions
def emp_payroll_cal(name,basic_sa,city_t,desig):
    print("---------------------------------------------------------------------------")
    print("Employement Payroll Calculation")
    if city_t.lower() == "metro":
        hra = basic_sa*0.24
    elif city_t.lower() =="tier1":
        hra = basic_sa*0.18
    else:
        hra = basic_sa*0.12

    da = basic_sa*0.12

    if desig.lower() =="senior manager" or desig.lower()== "manager":
        convenient_allowance = 10000
    else:
        convenient_allowance = 5000

    gross_salary = basic_sa + hra + da + con_allowance

    #deduction

    pf = basic_sa * 0.12
    income_tax = gross_salary * 0.1
    total_deduction = pf+income_tax
    net_sal = gross_salary - total_deduction

    print(f"Employee name: {name}")
    print(f"Basic salary of a employee: ₹{basic_sa:.2f}")
    print(f"HRA :₹{hra:.2f}")
    print(f"DA or Special Allowance: ₹{da:.2f}")
    print(f"Convenient Allowance: ₹{convenient_allowance:.2f}")
    print(f"Gross salary of a employee: ₹{gross_salary:.2f}")
    print(f"PF of the employee: ₹{pf:.2f}")
    print(f"Income tax of the employee: ₹{income_tax:.2f}")
    print(f"Net Salary : ₹{net_sal}")
    print("---------------------------------------------------------------------------")


emp_name = input("Enter your name: ")
b_sal = int(input("Ente your Basic Salary: "))
ciy__type = input("Enter the city type (metro/tier1/others): ")
designation = input("Enter your designation : ")

emp_payroll_cal(emp_name,b_sal,ciy__type,designation)