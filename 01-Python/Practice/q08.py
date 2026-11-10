text = input("Enter a text: ")

new = ""

for i in range(1,len(text)+1):

    new += text[-i]

if text == new:

    print("palindrome")

else:

    print("Not palindrome")

