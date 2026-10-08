# Beau Brazeau
# 10/4/2026
# Homework 2

# Loan Amortization
 
# 1. Inputs
principal = float(input("Enter the loan amount ($): "))
annual_rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the loan term (years): "))
 

 
# 2. Processing
# Convert the annual rate to a decimal, then to a monthly rate
monthly_rate = annual_rate / 100 / 12
 
# Total number of monthly payments
num_payments = years * 12
 
# Monthly payment formula
monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                  ((1 + monthly_rate) ** num_payments - 1)
 
 
# 3. Output
print()
print(f"Monthly Payment: ${monthly_payment:,.2f}")
print()
 
# Table header
print(f"{'Month':>5} {'Payment':>10} {'Principal':>12} {'Interest':>10} {'Balance':>12}")
 
# Table rows
balance = principal
 
for month in range(1, num_payments + 1):
    interest = balance * monthly_rate
    principal_paid = monthly_payment - interest
    balance = balance - principal_paid
 
    # Avoid printing a tiny negative number like -0.00 on the last month
    if abs(balance) < 0.005:
        balance = 0
 
    print(f"{month:5} {monthly_payment:10,.2f} {principal_paid:12,.2f} {interest:10,.2f} {balance:12,.2f}")
 