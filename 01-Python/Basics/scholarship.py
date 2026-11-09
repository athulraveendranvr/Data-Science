"""
Write a Python program to determine whether a student is eligible for a scholarship.

The program should accept:

Student Mark
Family Income
Rules
If the mark is 80 or above
Check the family income.
If the income is less than or equal to ₹2,00,000, the student is eligible for a Full Scholarship.
Otherwise, the student is eligible for a Partial Scholarship.
If the mark is between 60 and 79:
If the income is less than or equal to ₹1,00,000, the student is eligible for a Partial Scholarship.
Otherwise, No Scholarship.
If the mark is below 60:
No Scholarship.

"""

mark = int(input("Enter Your mark: "))

income = int(input("Enter your income: "))

if mark >= 80:

    if income <= 200000:

        print("You are eligible for full scholarship")

    else:

        print("You are not eligible for full scholarship")

elif mark >= 60 and mark <= 79:

    if income <= 100000:

        print("You are eligible for partial scholarship")

    else:

        print("You are not eligible for scholarship")

else:

    print("You are not eligible for scholarship")
