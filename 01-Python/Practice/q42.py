numbers = []

for i in range(5):

    try:

        n = int(input("Enter the numbers: "))

    except ValueError:

        print("Numbers only")

    else:

        numbers.append(n)

print(numbers)

