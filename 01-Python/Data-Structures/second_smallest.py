# wap to get the second smallest fron the guven list

numbers = [10,2,3,1,4,23,33,21]

smallest = float("inf")

second_smallest = float("inf")

for i in numbers:

    if i < smallest and i < second_smallest:

        second_smallest = smallest

        smallest = i

    elif i < smallest and i > second_smallest:

        second_smallest = i

print(smallest,second_smallest)

