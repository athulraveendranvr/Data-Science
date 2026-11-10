numbers = []

total = 0

average = 0

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for number in numbers:

    total += number

average = total//len(numbers)

for j in numbers:

    if j > average:

        print(j)