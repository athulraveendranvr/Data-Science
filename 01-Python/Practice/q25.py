numbers = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

largest = numbers[0]

smallest = numbers[0]

for number in numbers:

    if number > largest:

        largest = number

    if number < smallest:

        smallest = number

print(largest,smallest)