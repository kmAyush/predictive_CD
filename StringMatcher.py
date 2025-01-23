from Levenshtein import *
class StringMatcher:
    
    def __init__(self, isjunk=None, a='', b=''):
        if isjunk:
            self._isjunk = isjunk
        self.set_seqs(a, b)
        self.reset_cache()

    def set_seqs(self, a, b):
        self._a = a
        self._b = b
        self.reset_cache()

    def set_seq1(self, a):
        self.set_seqs(a, self._b)
        self.reset_cache()

    def set_seq2(self, b):
        self.set_seqs(self._a, b)
        self.reset_cache()

    def get_opcodes(self):
        if not self._opcodes:
            if self._editops:
                self._opcodes = opcodes(self._editops, self._a, self._b)
            else:
                self._opcodes = opcodes(self._a, self._b)
        return self._opcodes
    
    def get_matching_blocks(self):
        if not self._matching_blocks:
            self._matching_blocks = matching_blocks(self.get_opcodes(), self._a, self._b)
        return self._matching_blocks
    
    def get_editops(self):
        if not self._editops:
            if self._opcodes:
                self._editops = editops(self._opcodes, self._a, self._b)
            else:
                self._editops = editops(self._a, self._b)
        return self._editops

    def ratio(self):
        if not self._ratio:
            self._ratio = ratio(self._a, self._b)
        return self._ratio
    
    def distance(self):
        if not self._distance:
            self._distance = distance(self._a, self._b)
        return self._distance
    
    def quick_ratio(self):
        # This is usually quick enough :o)
        if not self._ratio:
            self._ratio = ratio(self._a, self._b)
        return self._ratio

    def real_quick_ratio(self):
        len1, len2 = len(self._a), len(self._b)
        return 2.0 * min(len1, len2) / (len1 + len2)
    
    def reset_cache(self):
        self._matching_blocks = None
        self._opcodes = None
        self._editops = None
        self._ratio = None
        self._distance = None