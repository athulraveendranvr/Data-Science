n = int(input("Enter a number: "))

t = n

length = len(str(n))

sum_of_digits = 0

while n > 0:

    digit = n % 10

    sum_of_digits += digit ** length

    n//=10

print(f"Armstrong"if t == sum_of_digits else"Not armstrong")