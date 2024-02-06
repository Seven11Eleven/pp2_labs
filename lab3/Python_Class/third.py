class Shape:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width
        
    def area(self):
        print(self.length*self.width)
    
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)


rect = Rectangle(5,6)
rect.area()
