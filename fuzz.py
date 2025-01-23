from StringMatcher import StringMatcher
import sys
def ratio(a, b):
    m = StringMatcher(None, a, b)
    return round(100*m.ratio(),2)