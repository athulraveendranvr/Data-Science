numbers = []

smallest = float("inf")

second_smallest = float("inf")

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for number in numbers:

    if number < smallest and number < second_smallest:

        second_smallest = smallest

        smallest = number

    elif number > smallest and number < second_smallest:

        second_smallest = number

print(smallest,second_smallest)

