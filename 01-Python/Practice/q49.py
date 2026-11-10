class Employee():

    def __init__(self,name,salary):

        self.name = name

        self.salary = salary

    def add_salary(self,amount):

        self.salary += amount

    def show_details(self):

        print(self.name)

        print(self.salary)

obj = Employee("Rahul",20000)

obj.add_salary(5000)

obj.show_details()