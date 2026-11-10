numbers = []

even = []

odd = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for number in numbers:

    if number % 2 == 0:

        even.append(number)

    else:

        odd.append(number)

print(even)
print(odd)