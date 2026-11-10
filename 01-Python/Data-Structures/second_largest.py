# wap to get the second largest from the list of numbers

numbers = [-5, -2, -7, -1, -8, -6]

if numbers[0]>numbers[1]:

    largest = numbers[0]

    sec_lar = numbers[1]

else:
    
    largest = numbers[1]

    sec_lar = numbers[0]

for i in numbers:

    if i > largest and i > sec_lar:

        sec_lar = largest

        largest = i
    
    elif i < largest and i > sec_lar:

        sec_lar = i

print(sec_lar)
    
        
            



