class FilerReader():
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            f = open(self.path, 'r')
        except IOError:
            print('error occured')
            return ''
        else:
            return f.read()
