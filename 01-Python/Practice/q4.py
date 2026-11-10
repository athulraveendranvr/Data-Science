numbers = []

even_count = 0

odd_count = 0

for i in range(5):

    n = int(input("Enter a num: "))

    numbers.append(n)

for number in numbers:

    if number % 2 == 0:

        even_count += 1

    else:

        odd_count += 1

print(even_count)
print(odd_count)