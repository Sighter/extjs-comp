

class StringHangingIterator(object):

    def __init__(self, string):
        self.string = string
        self.idx = 0

    def __iter__(self):
        return self

    def next(self):
        if self.idx < len(self.string):
            return self.string[self.idx]
        else:
            raise StopIteration
