# visuals.py

import tkinter as tk
from color4 import color4

APP_ICON="media\\app_icon.ico"

class MAIN_GUI:
    def __init__(self,width,height):
        self.root=tk.Tk()
        self.root.iconbitmap(APP_ICON)
        self.root.geometry(f"{width}x{height}")
        self.form=tk.Frame(self.root)
        self.form.grid()
        self.canvas=tk.Canvas(self.root,width=width-(width*0.05),height=height-(height*0.05))
        self.canvas.grid()
    def setup(self,mat):
        x1=5
        y1=5
        x2=10
        y2=10

        for i in range(mat.res_h):
            x1=5
            x2=10
            for k in range(mat.res_w):
                c=color4(mat.pixels[i][k][0]*255,mat.pixels[i][k][1]*255,mat.pixels[i][k][2]*255,mat.pixels[i][k][3])
                colorcode=c.hex()
                if(i==2):
                    print(c.r,c.g,c.b,f"i={i},k={k},#{colorcode}")
                    
                self.canvas.create_rectangle(x1,y1,x2,y2,fill=f"#{colorcode}",outline="")
                x1+=5
                x2+=5
            y1+=5
            y2+=5
    def run_normally(self):
        self.root.mainloop()
    def run(self,mat):
        self.setup(mat)     
        #colorcode="0C0000"
        #self.canvas.create_rectangle(5,5,10,10,fill=f"#{colorcode}",outline="")
        self.root.mainloop()
        
        