nums = []

flag = False

count = 0

for i in range(5):

    n = int(input("Enter the numbers:"))

    nums.append(n)

numbers = tuple(nums)

search = int(input("Enter the number to search: "))

for i in numbers:

    if i == search:

        count += 1

        flag = True

if flag:

    print(f"{search} exists {count} times")

else:

    print("Not found")
