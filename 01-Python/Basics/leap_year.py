"""
wap a prgm to check whether a year is leap or not

century year 2000,1900,...

conditions:-
divisible by 100
divisible by 400

non century year

conditions:-
not divisible by 100
divisible by 4

"""

year = int(input("Enter year: "))

# if year % 100 != 0 and year % 4 ==0 or year % 400 == 0:

#     print("Leap year")

# else:

#     print("Not leap year")

# ternary

print(f"{year} is leap year" if year % 100 != 100 and year % 4 == 0 or year % 400 == 0 else f"{year} is not leap year")

