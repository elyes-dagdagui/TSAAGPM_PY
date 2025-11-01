from matscreen import matscreen
from motionprocessing import exp_lerp_routine
from color4 import color4
from vector4 import vector4
from time import sleep as dly
class shaderbasic:
    def __init__(self,performance):
        self.performance=performance
    def slope2color(self, screen, color1, color2, slope, dir):
        ## vertical direction
        
        if(dir==0):
            eps=(1/screen.res_h)
            for i in range(screen.res_w):
                x=0
                for k in range(screen.res_h):
                    screen.pixels[k][i][0]=exp_lerp_routine(color1.r,color2.r,slope,x)
                    screen.pixels[k][i][1]=exp_lerp_routine(color1.g,color2.g,slope,x)
                    screen.pixels[k][i][2]=exp_lerp_routine(color1.b,color2.b,slope,x)
                    screen.pixels[k][i][3]=exp_lerp_routine(color1.a,color2.a,slope,x)
                    x=x+eps
        screen.save("matrix001.txt")