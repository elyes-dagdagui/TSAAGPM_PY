import math
class vector3:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
    def set(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def magnitude(self):
        x=self.x
        y=self.y
        z=self.z
        return math.sqrt(x*x+y*y+z*z)
    def normalized(self):
        m=self.magnitude()
        v=vector3()
        v.set(self.x/m,self.y/m,self.z/m)
        return v
    def get3(self):
        return [self.x,self.y,self.z]