a = []

for i in range(5):

    n = int(input("Enter a num:"))

    a.append(n)

largest = a[0]
smallest = a[0]

for i in a:

    if i > largest:

        largest = i

    if i < smallest:

        smallest = i

print(largest)
print(smallest)