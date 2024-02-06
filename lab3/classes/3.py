class Shape:
    def __init__(self, s_length, s_width):
        self.length = s_length
        self.width = s_width

class Rectangle(Shape):
    def __init__(self, r_length, r_width):
        Shape.__init__(self, r_length, r_width)
    
    def area(self):
        print(self.length * self.width)

p1 = Rectangle(4, 4)
p1.area()