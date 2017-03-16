# coding: utf8
from fractions import Fraction
from units import *


if __name__ == '__main__':
    C4 = Celsius(4)
    mc = Milli(Celsius)
    print(C4.convert_to(mc))


