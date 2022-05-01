from contextlib import contextmanager


class OpenFileV:
    def __init__(self, filename,vmist):
        self.filename = filename
        self.vmist = vmist

    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.file.write(self.vmist)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def open_file_v(nam, vmist):
    f = open(nam, 'w')
    f.write(vmist)
    yield f
    f.close()

string = 'hello I`m file'
with OpenFileV('uss.txt', string):
    pass

string = 'as for me'
with open_file_v('uss.txt', string):
    pass


