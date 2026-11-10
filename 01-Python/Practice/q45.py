def largest_num(*nums):

    largest = nums[0]

    for i in nums:

        if i > largest:

            largest = i

    return largest

print(largest_num(1,2,3,4,5))