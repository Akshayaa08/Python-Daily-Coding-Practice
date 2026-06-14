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

import sqlite3
print("-" * 80)
print("Star Health Insurance")

import sqlite3

conn = sqlite3.connect("health_insurance.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    age INTEGER,
    bp BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

customer_name = input("Enter your name: ")
cust_age = int(input("Enter your age: "))
cond = input("Do you have BP? (yes/no): ").lower()

if cond == "yes":
    bp_value = True
else:
    bp_value = False

cursor.execute("""
INSERT INTO customer_details (name, age, bp)
VALUES (?, ?, ?)
""", (customer_name, cust_age, bp_value))


conn.commit()

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

            if service in plans[customer_plan]["services"]:
                print(f"{service} is covered by insurance")
                insurance_cover += cost * 0.80
                patient_pay += cost * 0.20

            else:
                print(f"{service} is NOT covered in this plan")
                print("Customer must pay 100%")
                patient_pay += cost

        else:
            print("Invalid service")

        
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