import os
from contextlib import contextmanager

class OpenFolderV:
    def __init__(self, foldername , *vmist):
        self.foldername = foldername
        self.vmist = vmist

    def __enter__(self):
        try:
            self.folder = os.mkdir(self.foldername)
        except FileExistsError:
            print('FileExistsError')
            return FileExistsError
        for i in self.vmist:
            try:
                os.replace(f"{i}", f'{self.foldername}/{i}' )
            except:
                print("FileNotFoundError")
                return self.foldername

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

@contextmanager
def open_folder_v(nam, *files):
    trigger = 0
    try:
        os.mkdir(nam)
    except:
        print('FileExistsError')
        trigger = 1
    if trigger == 0:
        try:
            for i in files:
                os.replace(f"{i}", f'{nam}/{i}')
        except:
            print('FileNotFoundError')
        yield
    else:
        yield 'oh no'
    print('stopped')


with open_folder_v('afiles', 'f.py', 'frff.py'):
    pass

with OpenFolderV('bfiles', 'bancomat.py', 'ddd.py'):
    pass