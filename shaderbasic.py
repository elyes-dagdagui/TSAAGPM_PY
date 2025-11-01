from matscreen import matscreen
from motionprocessing import exp_lerp_routine
from color4 import color4
from vector4 import vector4
from time import sleep as dly
def clamp(x,min,max):
    if(x<min):
        return min
    elif(x>max):
        return max
    else:
        return x
class shaderbasic:
    def __init__(self,performance):
        self.performance=performance
    def slope2color(self, screen, color1, color2, slope, dir):
        ## vertical direction
        
        if(dir==0):
            eps=0.01
            for i in range(screen.res_w):
                x=0
                for k in range(screen.res_h):

                    r=exp_lerp_routine(color1.r,color2.r,slope,x)

                    g=exp_lerp_routine(color1.g,color2.g,slope,x)

                    b=exp_lerp_routine(color1.b,color2.b,slope,x)

                    a=exp_lerp_routine(color1.a,color2.a,slope,x)
                    
                    screen.pixels[k][i][0]=r
                    screen.pixels[k][i][1]=g
                    screen.pixels[k][i][2]=b
                    screen.pixels[k][i][3]=a

                    #print(f"{color4(r*255,g*255,b*255,a*255).hex()}")
                    x=x+eps
