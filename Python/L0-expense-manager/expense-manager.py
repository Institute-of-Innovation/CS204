def display_header(text):
    print('-' * 50)
    print(text.upper())
    print('-' * 50)


print("Enter your monthly income:")
monthly_income = int(input())
print("Enter the interest rate of the bank for your savings:")
interest_rate = float(input())

print("Enter the values for your expenses:")
input("Press Enter to continue...")

print("Enter your monthly rent or electricity bill:")
electricity = int(input())
print("Enter your monthly food expenses:")
food = int(input())
print("Enter your vehicle expenses:")
vehicles = int(input())
print("Enter your mobile and internet expenses:")
mobile_internet = int(input())
print("Enter your local expenses:")
local = int(input())
print("Enter your other expenses:")
other = int(input())

total_expenses = electricity + food + vehicles + mobile_internet + local + other
savings = monthly_income - total_expenses

display_header("Your Expenses and Savings")
print("Your total expenses are:", total_expenses)
print("Your savings are:", savings)

yearly_savings = savings * 12
yearly_expenses = {
    "Electricity or rent": electricity ,
    "Food": food ,
    "Vehicles": vehicles ,
    "Mobile & Internet": mobile_internet ,
    "Local": local ,
    "Other": other
}
display_header("")
input("press enter -----         ")
display_header("Yearly Summary")
print("Yearly Expenses:")
for key, value in yearly_expenses.items():
    print(key, ":", value*12)
print("Total income in a Year:",monthly_income*12)
print("Total expense in a Year:", total_expenses )
print("Total Savings in a Year:", yearly_savings)
display_header("")


input("press enter -----         ")
print("Enter 1 to calculate savings over multiple years:\nEnter 2 to see percentage of expense")
display_header("")
choice = int(input("enter the choice"))

if choice == 1:
    print("For how many years do you want to see your savings?")
    years = int(input())
    total_savings = yearly_savings
    total_interest = 0

    for _ in range(years):
        interest_earned = (interest_rate / 100) * total_savings
        total_savings += interest_earned
        total_interest += interest_earned

    print("Your total savings after", years, "years will be:", total_savings)
    print("Total interest earned:", total_interest)
elif choice == 2:
    print("\n\nThe percentage are :-")
    for key, value in yearly_expenses.items():
        print(key, " : ", (value/(monthly_income))*100,"%")
    print("total_expenses : ", (total_expenses/(monthly_income))*100,"%")

