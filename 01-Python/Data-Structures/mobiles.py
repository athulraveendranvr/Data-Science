mobiles = {"Apple":{"model":"iPhone 13", "price":130000,"color":"black"}, 
          "Samsung":{"model":"Galaxy S21", "price":95000 ,"color":"white"},
          "Google":{"model":"Pixel 6", "price":40000, "color":"black"}
          }


# wap to print the model and price of each mobile in the dictionary

# new = {}

# for i in mobiles:

#     new[i][mobiles[i] = ["model"],mobiles[i]["price"]]

# print(new)

# {'Apple': ['iPhone 13', 130000], 'Samsung': ['Galaxy S21', 95000], 'Google': ['Pixel 6', 40000]}

# wap to get the mobiles model name which have price in between 50k and 1lakh

new = {}

for i in mobiles:

    if mobiles[i]["price"] > 50000 and mobiles[i]["price"] < 100000:

        new[i] = mobiles[i]["price"]

print(new)
        
# wap to get the mobiles which have the price above 90k and color is black

new = []

for i in mobiles:

    if mobiles[i]["price"] > 90000 and mobiles[i]["color"] == "black":

        new.append(i)

print(new)