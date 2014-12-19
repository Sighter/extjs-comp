
class BaseContruct(object):
    """docstring for BaseContruct"""
    def __init__(self, arg):
        self.arg = arg

    def expand(self):
        raise NotImplementedError

    def get_unrevealed_tokens(self):
        return []