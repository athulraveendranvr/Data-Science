a = 0

b = 1

n = int(input("Enter the range: "))

print(a,b,end=" ")

for i in range(n-2):

    c = a + b #1

    a = b #1

    b = c #1

    print(c,end=" ")

