

class StringHangingIterator(object):

    def __init__(self, string):
        self.string = string
        self.cutidx = 1

    def __iter__(self):
        return self

    def next(self):
        if self.cutidx <= len(self.string):
            s = self.string[:self.cutidx]
            self.cutidx += 1
            return s
        else:
            raise StopIteration

    def consume(self):
        s = self.string[self.cutidx - 1:]
        self.string = s
        self.cutidx = 1
       
