# coding: utf8
"""
Module containing internal utility functions.
"""
import collections
from fractions import Fraction


def get_all_subclasses(cls):
    """
    Get all subclasses of given class. 
    """
    for subclass in cls.__subclasses__():
        yield subclass
        yield from get_all_subclasses(subclass)


def fraction_to_str(f, prec=5, auto=True):
    """
    Convert Fraction to str with given precision. 
    """
    r = collections.deque()
    if f < 0:
        r.append('-')
        f = -f
    x = 1
    while 10 ** x < f:
        x += 1
    while x > 0 and x > -prec:
        x -= 1
        w = Fraction(10**x)
        f, d = f % w, f // w
        r.append(str(int(d)))
    while x > 0:
        x -= 1
        r.append('0')
    if (f == 0 and auto) or (x <= -prec):
        return ''.join(r)
    r.append('.')
    while x > -prec:
        x -= 1
        w = Fraction('1/%s' % (10**-x))
        f, d = f % w, f // w
        r.append(str(int(d)))
        if f == 0 and auto:
            break
    return ''.join(r)
