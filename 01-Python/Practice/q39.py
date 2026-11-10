numbers = set()

for i in range(5):

    n = int(input("Enter the numbers: "))

    numbers.add(n)

search = int(input("Enter the number to search: "))

flag = False

for i in numbers:

    if i == search:

        print("Found")

        flag = True

if flag == False:

    print("Not found")