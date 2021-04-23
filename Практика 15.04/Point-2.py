class Point():
    
    def __init__(self, x = None, y = None):
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


f = Point()
print(f.getXY())
f.Show()
