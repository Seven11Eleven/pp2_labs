class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, first, second):
        print(abs(first-second))

point1 = Point(3, 4)
point2 = Point(5, 12)

point1.show()
point2.show()

point1.move(2, 3)
point1.show()

point2.dist(6, point2.x)
        