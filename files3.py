import os
from contextlib import contextmanager

class OpenFolderV:
    def __init__(self, foldername , *vmist):
        self.foldername = foldername
        self.vmist = vmist
        self.homedir = os.getcwd()

    def __enter__(self):
        self.folder = os.mkdir(self.foldername)
        os.chdir(self.foldername)
        for i in self.vmist:
            file = open(i, 'w')
        return self.vmist
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

@contextmanager
def open_folder_v(nam, *files):
    dir1 = os.getcwd()
    trigger = 0
    try:
        os.mkdir(nam)
        os.chdir(nam)
    except:
        raise FileExistsError
    if trigger == 0:
        for i in files:
            file = open(i, 'w')
        yield
        os.chdir(dir1)
    else:
        yield 'oh no'


with open_folder_v('ffiles', 'f.txt', 'frff.txt'):
    pass

with OpenFolderV('bfiles', 'bant.txt', 'just.txt'):
    pass