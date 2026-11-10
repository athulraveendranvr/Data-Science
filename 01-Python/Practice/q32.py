numbers = []

new = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for i in numbers.copy():

    temp = numbers.pop(numbers.index(i))

    if temp in numbers and temp not in new:

        new.append(temp)

for i in new:

    print(i)

