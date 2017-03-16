# coding: utf8
from fractions import Fraction
import typing
from .core import ValueType, Unit


class Temperature(ValueType):
    pass


class Kelvin(Unit):
    value_type = Temperature
    display_name = 'Kelvin'
    short_name = 'K'


class Celsius(Unit):
    value_type = Temperature
    display_name = 'Celsius'
    short_name = '°C'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value - Fraction('273.15')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value + Fraction('273.15')


class Fahrenheit(Unit):
    value_type = Temperature
    display_name = 'Fahrenheit'
    short_name = '°F'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return Fraction('32') + Fraction('1.8') * (value - Fraction('273.15'))

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return Fraction('5/9') * (value - Fraction('32')) + Fraction('273.15')

