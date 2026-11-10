keys = ["name","place","course"]

values = ["Arun","Kochi","Python"]

def combine(list1,list2):

    new = {}

    for i in range(len(list1)):

        new[list1[i]] = list2[i]

    return new

print(combine(keys,values))