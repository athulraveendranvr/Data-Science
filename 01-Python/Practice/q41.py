try:

    n = 100
    n2 = int(input("Enter a number to divide"))
    result = n/n2


except ValueError:

    print("Numbers only")

except ZeroDivisionError:

    print("Cannot be divided by zero")

else:

    print(result)

finally:

    print("program completed")