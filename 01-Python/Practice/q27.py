numbers = []

neg_count = 0

zero_count = 0

pos_count = 0

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for number in numbers:

    if number < 0:

        neg_count += 1

    elif number == 0:

        zero_count += 1

    else:

        pos_count += 1

print(f"Positive = {pos_count}\nNegative = {neg_count}\nZero = {zero_count}")

