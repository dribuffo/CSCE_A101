'''You're working with a simple budgeting program. You have received input from a user, and now you
need to perform type conversions to ensure that the data can be used for calculations. Given the
following user inputs, convert them to the appropriate data types and print the results:

I. The user entered their monthly income as a string: "2500.50". Convert this string to a floatingpoint number and print it.

II. The user entered the number of bills they have to pay this month as an integer but as a string:
"5". Convert this string to an integer and print it.

III. The user entered the amount they spent on groceries this week as a floating-point number
but as a string: "150.75". Convert this string to a floating-point number and print it.'''

# I:
monthly_income = input("Enter your monthly income: ")
monthly_income_float = float(monthly_income)
print(monthly_income_float)

# II:
num_bills = input("Input the number of bills you have this month: ")
num_bills_int = int(num_bills)
print(num_bills_int)

# III:
grocery_bill = input("Enter the cost of your groceries this week: ")
grocery_bill_float = float(grocery_bill)
print(grocery_bill_float)