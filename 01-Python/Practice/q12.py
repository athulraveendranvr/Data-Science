def is_prime(number):

    for i in range(2,number):

        if number % i == 0:

            return False

            break

    else:

        return True

n = int(input("Enter a number: "))

if is_prime(n) == True:

    print("Prime")

else:

    print("Not prime") 

