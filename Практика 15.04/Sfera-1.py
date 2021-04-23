import math
class Spher (object) :
    def __init__(self, r = None, x = None, y = None, z = None):
        if r == None:
            self.r = 1; self.x = 0; self.y = 0; self.z = 0 
        elif x == None:
            self.r = r; self.x = 0; self.y = 0; self.z = 0
        else:
            self.r = r; self.x = x; self.y = y; self.z = z
    def volume(self):
        return 4/3 * math.pi * self.r**3
    def square(self):
        return 4 * math.pi * self.r**2
    def radius(self):
        return self.r
    def center(self):
        return (self.x, self.y, self.z)
    def is_radius(self, r):
        self.r = r
        return r
    def is_center(self, x, y, z):
        self.x = x; self.y = y; self.z = z
        return x, y, z
    def point(self, x, y, z):
            return ( self.x - x ) ** 2 + ( self.y - y ) ** 2 + ( self.z - z ) ** 2 <= self.r ** 2
        
func = Spher(13, -1, -2, 24)
print(func.volume(),func.square(),func.radius(), func.center(),func.is_radius(5),func.is_center( -2 , 1 , 8 ),func.point( 6 , 7 , 9 ),sep = "\n")
