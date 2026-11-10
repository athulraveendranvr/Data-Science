file = open("new.txt","w")

for i in range(5):

    n = input("Enter 5 students: ")

    file.write(f"{n}\n")

file.close()

file2 = open("new.txt","r")

content = file2.read()

names = content.splitlines()

flag = False

for i in names:

    if i[0] == "a":

        print(i)

        flag = True

if flag == False:

    print("not found")