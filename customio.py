# customio.py

from pathlib import Path

def dir_create(dpath):
    Path(dpath).mkdir(exist_ok=True)

def file_create(fpath):
    f=open(fpath,"r")
    f.close()
    return f

def file_mread(fname):
    return open(fname,"r")

def file_mwrite(fname):
    return open(fname,"w")

def file_wappend(fname):
    return open(fname,"a")

def write_to_file(f,content):
    f.write(content)

def closefile(f):
    f.close()