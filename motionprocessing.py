from math import e

def expdecay(a1,a2,r,x):
    return a1 - ((a1-a2)*pow(e,x*r)*x*r)
def expamplifier(a1,a2,r,x):
    return a1 + ((a2-a1)*pow(e,x*r)*x*r)
def exp_lerp_routine(a1,a2,r,x):
    if(a1>a2):
        return expdecay(a1,a2,r,x)
    elif(a1<a2):
        return expamplifier(a1,a2,r,x)
    else:
        return a1