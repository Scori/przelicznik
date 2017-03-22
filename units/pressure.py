from fractions import Fraction
import typing
from .core import ValueType, Unit

class Pressure(ValueType):
    display_name = 'Pressure'

class Pascal(Unit):
    value_type = Pressure
    display_name = 'Pascal'
    short_name = 'Pa'

class Bar(Unit):
    value_type = Pressure
    display_name = 'Bar'
    short_name = 'bar'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value*Fraction('0.000010')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value/Fraction('0.000010')

class Atmosphere(Unit):
    value_type = Pressure
    display_name = 'Atmosphere'
    short_name = 'atm'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value/Fraction('101325')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value*Fraction('101325')

class Tor(Unit):
    value_type = Pressure
    display_name = 'Tor'
    short_name = 'mm Hg'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value/Fraction('133.3224')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value*Fraction('133.3224')

class Psi(Unit):
    value_type = Pressure
    display_name = 'Psi'
    short_name = 'psi'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value/Fraction('6894.75729')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value*Fraction('6894.75729')