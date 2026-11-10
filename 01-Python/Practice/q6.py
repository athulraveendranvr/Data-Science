text = input("Enter a text: ")

count = 0

vowels = "aeiou"

for i in text.lower():

    if i in vowels:

        count += 1

print(count)