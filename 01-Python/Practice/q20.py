numbers = []

ab = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for number in numbers:

    a = number

    count = 0

    for j in numbers:

        if j == a:

            count += 1

    if a not in ab:

        print(a,"=",count)

        ab.append(a)