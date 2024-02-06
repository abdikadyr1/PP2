class Points:
    def __init__(self, p1_x, p1_y, p2_x, p2_y):
        self.p1_x = p1_x
        self.p1_y = p1_y
        self.p2_x = p2_x
        self.p2_y = p2_y
        
    def show(self):
        print("current point: ", f"({self.p1_x}, {self.p1_y})")
        
    def move(self):
        print("point after moving: ", f"({self.p2_x}, {self.p2_y})")  
        
    def dist(self):
        d = ((self.p2_x - self.p1_x)**2 + (self.p2_x - self.p1_y)**2)**0.5
        print("distance: ", d)

x = float(input())
y = float(input())
x1 = float(input())
y1 = float(input())        
        
s = Points(x, y, x1, y1)
s.show()
s.move()
s.dist()