n = int(input("Enter the start: "))

n2 = int(input("Enter the finish: "))

for i in range(n,n2):

    for j in range(2,i):

        if i % j == 0:

            break

    else:

        print(i)

        