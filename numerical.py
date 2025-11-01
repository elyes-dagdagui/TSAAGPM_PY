HEX=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
def conv_dec_hex(dec,w):
    ss=""
    while(dec!=0):
        x=dec//16
        r=dec%16
        dec=dec//16
        ss=HEX[r]+ss
    if(w>0 and len(ss)<w):
        ss+="0"*(w-len(ss))
    return ss