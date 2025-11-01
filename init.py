from color4 import color4
from matscreen import matscreen
from shaderbasic import shaderbasic
def main():
    A1=color4(1,1,1,1)
    A2=color4(0,0,0,1)
    M1=matscreen(1200,1000)
    sb=shaderbasic(2)
    sb.slope2color(M1,A1,A2,0.5,0)
    #M1.save("matrix1.txt")

main()