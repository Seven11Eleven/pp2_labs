class Shape:
    def __init__(self, length = 0):
        self.length = length
        
    def area(self):
        print(self.length*self.length)
    
    
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)


square = Square(5)
square.area()
