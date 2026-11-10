numbers = []

numbers2 = []

new = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for i in range(5):

    n2 = int(input("Enter the numbers: "))

    numbers2.append(n2)

for i in range(len(numbers)):

    if numbers[i] in numbers2 and numbers[i] not in new:

        new.append(numbers[i])

print(new)



