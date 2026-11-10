numbers = []

positive = []

negative = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for number in numbers:

    if number > 0:

        positive.append(number)

    elif number < 0:

        negative.append(number)

print(positive)
print(negative)