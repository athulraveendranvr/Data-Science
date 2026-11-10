numbers  = []

flag = False

count = []

for i in range(5):

    n = int(input("Enter:" ))

    numbers.append(n)

search = int(input("Enter the element to search: "))

for i in range(len(numbers)):

    if numbers[i] == search:

        count.append(i)

        flag = True

if flag == True:

    for i in count:

        print(f"{search} was present on {i}")

else:

    print("element was not found")



