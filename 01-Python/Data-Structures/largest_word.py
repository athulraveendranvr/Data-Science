# wap to get the largest word from the string

string = "python is a programming language"

largest = 0

for i in string.split():

    if len(i) > largest:

        largest = len(i)

        element = i

print(element)