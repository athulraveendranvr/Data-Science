numbers = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

smallest = numbers[0]

for number in numbers:

    if number < smallest:

        smallest = number

print(smallest)