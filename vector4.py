import math
class vector4:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        self.w=0
    def set(self,x,y,z,w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w
    def magnitude(self):
        x=self.x
        y=self.y
        z=self.z
        w=self.w
        return math.sqrt(x*x+y*y+z*z+w*w)        
    def normalized(self):
        m=self.magnitude()
        v=vector4()
        v.set(self.x/m,self.y/m,self.z/m,self.w/m)
        return v
    def get4(self):
        return [self.x,self.y,self.z,self.w]