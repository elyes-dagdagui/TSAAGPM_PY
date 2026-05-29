# customio.py

from pathlib import Path

def dir_create(dpath):
    Path(dpath).mkdir(exist_ok=True)

def file_create(fpath):
    f=open(fpath,"r")
    f.close()
    return f