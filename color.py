# color.py

from vector3 import vector3
from numerical import conv_dec_hex
class color:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b
    def hex(self):
        return conv_dec_hex(self.r,2)+conv_dec_hex(self.g,2)+conv_dec_hex(self.b,2)
    def normalized(self):
        r=round(self.r/255,3)
        g=round(self.g/255,3)
        b=round(self.b/255,3)
        return [r,g,b]
    def vec3(self):
        v=vector3()
        v.set(self.r,self.g,self.b)
        return v 