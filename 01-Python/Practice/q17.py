n = int(input("Enter a number:"))

fi = int(input("Enter the number to search:"))

count = 0

while n > 0:

    digit = n % 10

    if digit == fi:

        count += 1

    n //= 10

print(count)



