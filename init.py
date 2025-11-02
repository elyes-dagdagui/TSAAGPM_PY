from color4 import color4
from matscreen import matscreen
from shaderbasic import shaderbasic
from visuals import MAIN_GUI
from motionprocessing import expamplifier, expdecay

WIDTH=400
HEIGHT=400
gui=MAIN_GUI(WIDTH,HEIGHT)

def main():
    A1=color4(1,0,0.75,1)
    A2=color4(1,1,0.75,1)
    M1=matscreen(WIDTH,HEIGHT)
    sb=shaderbasic(2)
    sb.slope2color(M1,A1,A2,3,0)
    M1.save_numerical("matrix001.txt")
    gui.run(M1)

main()