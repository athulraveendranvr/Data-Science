numbers = []

for i in range(5):

    n = int(input("Enter the numbers:"))

    numbers.append(n)

largest = float("-inf")

second_largest = float("-inf")

for number in numbers:

    if number > largest:

        largest = number

for j in numbers:

    if j < largest and j > second_largest:

        second_largest = j

print(largest,second_largest)



