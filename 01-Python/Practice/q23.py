numbers = []

new = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for j in range(len(numbers)-1,-1,-1):

    new.append(numbers[j])

print(new)

    