n = int(input("Enter the number: "))

factorial = 1

for i in range(n,1,-1):

    factorial *= i

print(factorial)