file = open("new.txt","w")

file.write("Python is easy")

file.close()

file2 = open("new.txt","a")

file2.write("\nIm learning python")

file2.close()

file3 = open("new.txt","r")

print(file3.read())

file3.close()
