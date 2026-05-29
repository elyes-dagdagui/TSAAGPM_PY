# matscreen.py

from color4 import color4
from vector4 import vector4
from numpy import array
from customio import *
import simpley as smply

PIXEL_LEVELS_CHAR  = ('#','+','*','-','.')
PIXEL_LEVELS_FLOAT = (0.75,0.5,0.25,0.1)


def get_pixel(brightness):
    return smply.itercheck(PIXEL_LEVELS_FLOAT,PIXEL_LEVELS_CHAR,brightness,smply.supeq)

class matscreen:
    def __init__(self,res_w,res_h):
        self.res_w=res_w
        self.res_h=res_h
        self.ratio=res_w/res_h
        #self.pixels=[[[1,1,1,1]]*res_w]*res_h
        self.pixels=array([[array([float()]*4)]*res_w]*res_h)
    def fill(self,color):
        for i in range(self.res_h):
            for k in range(self.res_w):
                self.pixels[i][k]=color
    def save(self,name):
        f=file_mwrite(name)
        l=""
        for i in range(self.res_h):
            for k in range(self.res_w):
                v=color4(self.pixels[i][k][0],self.pixels[i][k][1],self.pixels[i][k][2],self.pixels[i][k][3])
                x=v.fbrightness()
                l=f"{smply.concat(l,get_pixel(x))} "
                ##l = l + str(self.pixels[i][k][0]) +", "+ str(self.pixels[i][k][1]) +"," + str(self.pixels[i][k][2]) + " | "
            write_to_file(f,l)
            l=""
        closefile(f)
    def save_numerical(self,name):
        f=file_mwrite(name)
        l=""
        for i in range(self.res_h):
            for k in range(self.res_w):
                v=color4(self.pixels[i][k][0],self.pixels[i][k][1],self.pixels[i][k][2],self.pixels[i][k][3])
                x=v.fbrightness()
                l = l + f"[{round(v.r,2)},{round(v.g,2)},{round(v.b,2)},{round(v.a,2)}] | {round(x*100,2)}%, "
            write_to_file(f,l)
            l=""
        closefile(f)
        