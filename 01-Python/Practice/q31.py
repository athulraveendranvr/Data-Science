numbers = []

new = []

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.append(n)

for i in range(len(numbers)):

    for j in range(i+1,len(numbers)):

        if numbers[i] + numbers[j] == 10:

            temp = []

            temp.append(numbers[i])

            temp.append(numbers[j])

            if temp not in new:

                new.append(temp)

print(new)

        



