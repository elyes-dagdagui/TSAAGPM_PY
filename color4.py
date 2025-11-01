from vector4 import vector4
from numerical import conv_dec_hex
class color4:
    def __init__(self,r,g,b,a):
        self.r=r
        self.g=g
        self.b=b
        self.a=a
    def hex(self):
        return conv_dec_hex(self.r,2)+conv_dec_hex(self.g,2)+conv_dec_hex(self.b,2)
    def normalized(self):
        r=round(self.r/255,3)
        g=round(self.g/255,3)
        b=round(self.b/255,3)
        return [r,g,b,self.a]
    def fbrightness(self):
        return (self.r+self.g+self.b)/3
    def vec4(self):
        v=vector4()
        v.set(self.r,self.g,self.b,self.a)
        return v 