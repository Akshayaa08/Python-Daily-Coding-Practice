# # fruits ={"apple","orange","banana","coconut","coconut"}
# # print(fruits) #no duplicates


# def emp_payroll_cal(name,basic_sa,city_t,desig):
#     print("---------------------------------------------------------------------------")
#     print("Employement Payroll Calculation")
#     if city_t.lower() == "metro":
#         hra = basic_sa*0.24
#     elif city_t.lower() =="tier1":
#         hra = basic_sa*0.18
#     else:
#         hra = basic_sa*0.12

#     da = basic_sa*0.12

#     if desig.lower() =="senior manager" or desig.lower()== "manager":
#         con_allowance = 10000
#     else:
#         con_allowance = 5000

#     gross_salary = basic_sa + hra + da + con_allowance

#     #deduction

#     pf = basic_sa * 0.12
#     income_tax = gross_salary * 0.1
#     net_sal = gross_salary -(pf+income_tax)

#     print(f"Employee name: {name}")
#     print(f"Basic salary of a employee: ₹{basic_sa:.2f}")
#     print(f"HRA :₹{hra:.2f}")
#     print(f"DA or Special Allowance: ₹{da:.2f}")
#     print(f"Gross salary of a employee: ₹{gross_salary:.2f}")
#     print(f"PF of the employee: ₹{pf:.2f}")
#     print(f"Income tax of the employee: ₹{income_tax:.2f}")
#     print(f"Net Salary : ₹{net_sal}")
#     print("---------------------------------------------------------------------------")


# emp_name = input("Enter your name: ")
# b_sal = int(input("Ente your Basic Salary: "))
# ciy__type = input("Enter the city type (metro/tier1/others): ")
# designation = input("Enter your designation : ")

# emp_payroll_cal(emp_name,b_sal,ciy__type,designation)

# Problem 3
# Health insurance plan
# to store the plan dictionary 
# plan a - star health - amount 10000 - service - general checkup and blood test
# plan b - star health plus - 250000 - service - general checkup, room accommodation, dental checkup and blood test
# plan c - star health pro - 50000 - general checkup, blood test, room accommodation, dental checkup, mri, x-ray, ct-scans 

# general checkup -400
# blood test-150
# room accommodation-5000
# dental checkup -400
# mri -5000 
# x-ray-2500 
# ct-scans-3500


# service covered - i am eligible
# USER - cust details - name, which plan, 

# Condition Check - if he has BP he will not be eligible for any services for 2 years
# sorry due to the your condition u are not eligible

# show the plan and ask the customer to select the plan, 
# invalid
# ask the cust to select the service and if not available then not available
# total cost of the service 

# basic plan but the customer want to pick mri scan, he can take but it will not be covered by the plan and it needs to be paid 100%
# message throws

# output
# selected plan 
# list of service taken
# total medical bill
# inside the plan
# insurance cover up from the total medical bill for 80% and remaining 20% by the patient 


print("-" * 80)
print("Star Health Insurance")

customer_name = input("Enter your name: ")

plans = {
    "star health": {
        "amount": 10000,
        "services": ["general checkup", "blood test"]
    },

    "star health plus": {
        "amount": 25000,
        "services": [
            "general checkup",
            "blood test",
            "room accommodation",
            "dental checkup"
        ]
    },

    "star health pro": {
        "amount": 50000,
        "services": [
            "general checkup",
            "blood test",
            "room accommodation",
            "dental checkup",
            "mri",
            "x-ray",
            "ct-scans"
        ]
    }
}

service_cost = {
    "general checkup": 400,
    "blood test": 150,
    "room accommodation": 5000,
    "dental checkup": 400,
    "mri": 5000,
    "x-ray": 2500,
    "ct-scans": 3500
}

# BP condition check
cond = input("Do you have BP? (yes/no): ").lower()

if cond == "yes":
    print("Sorry! You are not eligible for health insurance for 2 years.")

else:
    print("\nYou are eligible!")

    print("\nAvailable Plans:")
    for plan, details in plans.items():
        print(f"{plan.title()} : ₹{details['amount']}")

    customer_plan = input("\nSelect a plan: ").lower()

    if customer_plan not in plans:
        print("Invalid Health Insurance Plan")

    else:
        print(f"\nSelected Plan: {customer_plan.title()}")

        print("\nCovered Services:")
        for service in plans[customer_plan]["services"]:
            print(f"- {service}")

        service_count = int(input("\nEnter number of services: "))

        customer_services = {}
        insurance_cover = 0
        patient_pay = 0
        total_bill = 0

        for i in range(service_count):
            service = input(f"\nEnter service {i+1}: ").lower()

            if service in service_cost:
                cost = service_cost[service]
                customer_services[service] = cost
                total_bill += cost

                # Covered by plan
                if service in plans[customer_plan]["services"]:
                    print(f"{service} is covered by insurance")
                    insurance_cover += cost * 0.80
                    patient_pay += cost * 0.20

                # Not covered by plan
                else:
                    print(f"{service} is NOT covered in this plan")
                    print("Customer must pay 100%")
                    patient_pay += cost

            else:
                print("Invalid service")

        # Output
        print("\n" + "-" * 50)
        print("Insurance Summary")
        print("-" * 50)

        print(f"Customer Name: {customer_name}")
        print(f"Selected Plan: {customer_plan.title()}")

        print("\nServices Taken:")
        for service, cost in customer_services.items():
            print(f"{service} : ₹{cost}")

        print(f"\nTotal Medical Bill: ₹{total_bill:.2f}")
        print(f"Insurance Covers (80%): ₹{insurance_cover:.2f}")
        print(f"Patient Pays: ₹{patient_pay:.2f}")

print("-" * 80)