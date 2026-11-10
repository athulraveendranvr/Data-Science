a = []

for i in range(3):

    n = int(input("Enter a number:"))

    a.append(n)

if a[0] > a[1] and a[0] > a[2]:

    largest = a[0]

elif a[1] > a[0] and a[1] > a[2]:

    largest = a[1]

else:

    largest = a[2]

print(largest)

    

