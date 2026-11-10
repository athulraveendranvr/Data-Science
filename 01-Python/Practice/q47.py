class Rectangle():

    def __init__(self,length,breadth):

        self.length = length

        self.breadth = breadth

    def area(self):

        return (self.breadth * self.length)

obj = Rectangle(25,10)

print(obj.area())


