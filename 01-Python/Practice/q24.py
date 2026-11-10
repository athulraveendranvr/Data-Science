numbers = []

new = []

total = 0

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for number in numbers:

    total += number

print(total)