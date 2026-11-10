numbers = []

new = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for j in numbers:

    if j not in new:

        new.append(j)

print(new)

