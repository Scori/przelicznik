from fractions import Fraction
import typing
from .core import ValueType, Unit

class Power(ValueType):
    display_name = 'Power'

class Watt(Unit):
    value_type = Power
    display_name = 'Watt'
    short_name = 'W'

class Horsepower(Unit):
    value_type = Power
    display_name = 'Horsepower'
    short_name = 'hpm'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value/Fraction('735.49875')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value*Fraction('735.49875')