# simpley.py

def concat(str1,str2):
    return str1+str2
def sup(val1,val2):
    return val1>val2
def supeq(val1,val2):
    return val1>=val2
def inf(val1,val2):
    return val1<val2
def infeq(val1,val2):
    return val1<=val2

def itercheck(tuple1,tuple2,val,boolf):
    i=0
    while(i<len(tuple1)):
        if(boolf(val,tuple1[i])):
            return tuple2[i]
        i=i+1
    return ''
    