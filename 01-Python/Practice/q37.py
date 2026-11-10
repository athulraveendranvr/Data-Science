students = {}

for i in range(5):

    n = input("name:")

    m = int(input("Enter the mark:"))

    students[n] = m

flag = False

largest = float("-inf")

for i in students:

    if students[i] > largest:

        largest = students[i]

        key = i

        flag = True

print(key)

if flag == False:

    print("Not found")

        

    