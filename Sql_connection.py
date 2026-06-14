import sqlite3

print("-" * 80)
print("Star Health Insurance")

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
    print("\nSorry! You are not eligible for health insurance for 2 years.")

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

        file = open("insurance_output.txt", "a", encoding="utf-8")
        file.write("\n")
        file.write("=" * 80 + "\n")
        file.write("STAR HEALTH INSURANCE OUTPUT\n")
        file.write("=" * 80 + "\n")

        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Customer Age: {cust_age}\n")
        file.write(f"BP Condition: {'Yes' if bp_value else 'No'}\n")
        file.write(f"Selected Plan: {customer_plan.title()}\n")

        file.write("\nServices Taken:\n")
        for service, cost in customer_services.items():
            file.write(f"{service} : ₹{cost}\n")

        file.write(f"\nTotal Medical Bill: ₹{total_bill:.2f}\n")
        file.write(f"Insurance Cover (80%): ₹{insurance_cover:.2f}\n")
        file.write(f"Patient Pays: ₹{patient_pay:.2f}\n")

        file.write("=" * 80 + "\n")

        file.close()

        print("\nInsurance details saved in insurance_output.txt")

conn.close()

print("-" * 80)