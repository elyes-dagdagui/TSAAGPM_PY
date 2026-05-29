# init.py
# TSAAGPM(Techie's shader architecture and graphical processing model) >> 2D Basic shader computation model demo
# Project GitHub Repos : https://github.com/elyes-dagdagui/TSAAGPM_PY
# Developer Name       : ELYES DAGDAGUI
# Developer Email      : dagdaguielyes50@gmail.com
# Developer GitHub     : https://github.com/elyes-dagdagui

from color4 import color4
from matscreen import matscreen
from shaderbasic import shaderbasic
from visuals import MAIN_GUI
import customio

TEXT_PATH="text"
NUMERICAL_FORM_PATH="text\\matrix.txt"

customio.dir_create(TEXT_PATH)

WIDTH=400
HEIGHT=400
gui=MAIN_GUI(WIDTH,HEIGHT)
A1=color4(1,0,0.75,1)
A2=color4(1,1,0.75,1)
BLACK=color4(0,0,0,1)
LTBLUE=color4(0.67,0.84,0.9,1)
GRAY=color4(0.5,0.5,0.5,1)
RED=color4(1,0,0,1)

def main():
    M1=matscreen(WIDTH,HEIGHT)
    sb=shaderbasic(2)
    sb.slope2color(M1,A2,A1,0.7,2)
    M1.save_numerical(NUMERICAL_FORM_PATH)
    gui.setup(M1)
    gui.run_normally()

main()