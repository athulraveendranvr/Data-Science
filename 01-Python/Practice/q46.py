class Student():

    def __init__(self,name,mark):

        n = name

        m = mark

        self.name = n

        self.mark = m

    def print_name(self):

        return self.name

    def print_mark(self):

        return self.mark

obj = Student("rahul",80)

print(obj.print_name())
print(obj.print_mark())



