class Point():
    def __init__(self, x = None, y=None):
        if x == None:
            self.x = 0
        else:
           self.x = x
        if y == None:
            self.y = 0
        else:
            self.y = y
    def getXY(self):
        return [self.x, self.y]
    def Show(self):
        print(self.x, self.y)
        #print("(", self.x, "; ", self.y, ")")

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)
    def __eq__(self, other):
        return Point(self.x == other.x) and (self.y == other.y)
f1 = Point(12,10)
f2 = Point(9,7)
print(f1.getXY())
(f1+f2).Show()
(f1 - f2).Show()
(f1 * f2).Show()
(f1 / f2).Show()
print(f1 == f2)