#string = "AABBCDAB"

# find the first recursive char(repeating)

# find the count of recursuve chars

# find the first non recursive char

# def rec(text):

#     for i in text:

#         if text.count(i) > 1:

#             print(i)

#             break


# def rec(text):

#     new = ""

#     for i in text:

#         if text.count(i) > 1 and i not in new:

#             print(i,text.count(i))

#             new += i

def rec(text):

    for i in text:

        if text.count(i) == 1:

            print(i)

            break
         


rec("AABBCDAB")