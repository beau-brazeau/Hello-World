# Beau Brazeau
# 9/13/2026
# homework 1

# Sales Tax Calculator

# Ask the user for the price and quantity
price = float(input("Enter the item's price: $"))
quantity = int(input("Enter the quantity: "))
 
# Calculate subtotal
subtotal = price * quantity
 
# Apply 7.5% sales tax
tax = subtotal * 0.075
total = subtotal + tax
 
# Print the results to 2 decimals
print("")
print("--- Sales Tax Calculator ---")
print("Subtotal: $" + str(round(subtotal, 2)))
print("Tax Amount: $" + str(round(tax, 2)))
print("Total: $" + str(round(total, 2)))

# Employee Weekly Pay Calculator

#  ask the user for hourly wage and hours worked
wage = float(input("Enter the hourly wage: "))
hours = float(input("Enter the hours worked: "))

#check the overtime hours
if hours > 40:
    overtime_hours = hours - 40
    base_pay = 40 * wage
    overtime_pay = overtime_hours * wage * 1.5
# Calculate regular pay if there is no overtime
else:
    base_pay = hours * wage
    overtime_pay = 0
    
# add the base pay and overtime pay
total_pay = base_pay + overtime_pay

print("Base pay:", round(base_pay, 2))
print("Overtime pay:", round(overtime_pay, 2))
print("Total pay:", round(total_pay, 2))


# 3. Student Grade Categorizer
# ask user for their numeric grade

grade = float(input("Enter the student's grade: "))

# determine the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# print numeric and letter grade
print("Numeric grade:", grade)
print("Letter grade:", letter)


# 4. Bonus Eligibility Checker

# ask the user for hours worked and performance score hours
hours = float(input("Enter hours worked: "))
score = float(input("Enter performance score: "))

# Check if the employee qualifies for the bonus
if hours > 35 and score > 85:
    print("Congratulations! You earned a $100 bonus.")
    
# Print a message if the employee does not qualify
else:
    print("You are not eligible for the bonus.")

    if hours <= 35:
        print("More hours needed:", 36 - hours)

    if score <= 85:
        print("More points needed:", 86 - score)
