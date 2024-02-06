class Shape:
    def area(self):
        print(0)
    
class Square(Shape):
    def __init__(self, sq_length):
        self.length = sq_length
    def area(self):
        print(self.length**2)
        
p1 = Shape()
p2 = Square(5)
p1.area()
p2.area()