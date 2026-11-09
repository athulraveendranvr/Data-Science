# wap to get the price of the bike from user
# if the bike_price above 2lakh add 12% tax and show the total bill
# if the bike prive is above 1lakh and less than or equal to 2 lakh 
#   add 10 % tax and show th bill
# if less than 1 lakh add 7 % and show the bill

price = int(input("Enter a number: "))

if price > 200000:

    tax = price * 0.12 # interest= price * interest/100

    print("Total bill is ",price + tax) 

elif price > 100000 and price <= 200000:

    tax = price * 0.10

    print("Total bill is",price + tax)

else:

    tax = price * 0.07

    print("Total bill is ",price + tax)