# coding: utf8
from fractions import Fraction
from .core import ScaleUnit


class Prefix(ScaleUnit):
    pass


class Tera(Prefix):
    display_name = 'Tera'
    short_name = 'T'
    multiplier = Fraction('1000')**4


class Giga(Prefix):
    display_name = 'Giga'
    short_name = 'G'
    multiplier = Fraction('1000')**3


class Mega(Prefix):
    display_name = 'Mega'
    short_name = 'M'
    multiplier = Fraction('1000')**2


class Kilo(Prefix):
    display_name = 'Kilo'
    short_name = 'k'
    multiplier = Fraction('1000')**1


class One(Prefix):
    display_name = '-'
    short_name = ''
    multiplier = Fraction('1000')**0


class Milli(Prefix):
    display_name = 'Milli'
    short_name = 'm'
    multiplier = Fraction('1000')**-1


class Micro(Prefix):
    display_name = 'Micro'
    short_name = 'μ'
    multiplier = Fraction('1000')**-2


class Nano(Prefix):
    display_name = 'Nano'
    short_name = 'n'
    multiplier = Fraction('1000')**-3


class Pico(Prefix):
    display_name = 'Pico'
    short_name = 'p'
    multiplier = Fraction('1000')**-4


