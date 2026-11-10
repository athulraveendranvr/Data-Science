set1 = {1,2,3,4,5}

flag = False

n = 3

for i in set1.copy():

    if i == n:

        set1.remove(i)
        flag = True

if flag:

    print(set1)

else:

    print("Not found")
