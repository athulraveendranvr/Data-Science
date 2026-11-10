# define a function to check a given number is strong or not

# def strong(n):

# wap to check a number is strong

# strong number = sum of factoral of digits = number

# number = 145

# 1! + 4! + 5! = 145

def strong(number):

    sum = 0


    for i in str(number):

        fact = 1

        n = int(i)

        for j in range(1,n+1):

            fact *= j

        sum += fact

    print("strong" if sum == number else "Not strong")

strong(145)

        
