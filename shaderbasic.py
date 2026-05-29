# shaderbasic.py

from matscreen import matscreen
from motionfs import exp_lerp_routine
from color4 import color4
from vector4 import vector4
from numpy import array
from time import sleep as dly

def clamp(x,min,max):
    if(x<min):
        return min
    elif(x>max):
        return max
    else:
        return x

def RGBA_EXP_LERP_ROUTINE(color1,color2,slope,x):
    return array(
        [exp_lerp_routine(color1.r,color2.r,slope,x),
         exp_lerp_routine(color1.g,color2.g,slope,x),
         exp_lerp_routine(color1.b,color2.b,slope,x),
         exp_lerp_routine(color1.a,color2.a,slope,x)
         ]
    )

class shaderbasic:
    def __init__(self,performance):
        self.performance=performance
    def slope2color(self, screen, color1, color2, slope, dir):
        ## vertical direction
        eps=0.01
        if(dir==0):
            for i in range(screen.res_w):
                x=0
                for k in range(screen.res_h):
                    rgba=RGBA_EXP_LERP_ROUTINE(color1,color2,slope,x)
                    
                    screen.pixels[k][i][0]=rgba[0]
                    screen.pixels[k][i][1]=rgba[1]
                    screen.pixels[k][i][2]=rgba[2]
                    screen.pixels[k][i][3]=rgba[3]

                    #print(f"{color4(r*255,g*255,b*255,a*255).hex()}")
                    x=x+eps
        ## horizontal direction
        elif(dir==1):
            for i in range(screen.res_h):
                x=0
                for k in range(screen.res_w):
                    rgba=RGBA_EXP_LERP_ROUTINE(color1,color2,slope,x)

                    screen.pixels[i][k][0]=rgba[0]
                    screen.pixels[i][k][1]=rgba[1]
                    screen.pixels[i][k][2]=rgba[2]
                    screen.pixels[i][k][3]=rgba[3]

                    x=x+eps
        # diagonal top-left to bottom-right
        elif(dir==2):
            v=0
            for i in range(screen.res_h,-1,-1):
                j=i
                x=0
                for k in range(v):
                    rgba=RGBA_EXP_LERP_ROUTINE(color1,color2,slope,x)
                    screen.pixels[j][k][0]=rgba[0]
                    screen.pixels[j][k][1]=rgba[1]
                    screen.pixels[j][k][2]=rgba[2]
                    screen.pixels[j][k][3]=rgba[3]
                    x=x+eps
                    j=j+1
                v=v+1
            v=screen.res_w-1
            for i in range(1,screen.res_w):
                j=i
                x=0
                for k in range(v):
                    rgba=RGBA_EXP_LERP_ROUTINE(color1,color2,slope,x)
                    screen.pixels[k][j][0]=rgba[0]
                    screen.pixels[k][j][1]=rgba[1]
                    screen.pixels[k][j][2]=rgba[2]
                    screen.pixels[k][j][3]=rgba[3]
                    x=x+eps
                    j=j+1 
                v-=1
