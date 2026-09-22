"""
Problem:
Write a Python program to calculate an electricity bill.
Input the customer's name and the number of electricity units used.
Calculate and display the total bill using these rates:

- First 100 units: Rs. 5 per unit
- Next 100 units: Rs. 7 per unit
- Above 200 units: Rs. 10 per unit
"""

customer_name = input("Enter customer name: ")
units = int(input("Enter electricity units used: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("\nElectricity Bill")
print(f"Customer name: {customer_name}")
print(f"Units used: {units}")
print(f"Total bill: Rs. {bill}")
