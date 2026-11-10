numbers = []
even = []
odd = []

for i in range(5):

    n = int(input("Enter:"))

    numbers.append(n)

for i in numbers:

    if (i // 2) * 2 == i:

        even.append(i)   

    else:

        odd.append(i)

print(even)
print(odd)