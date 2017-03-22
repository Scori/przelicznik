from fractions import Fraction
import typing
from .core import ValueType, Unit

class Energy(ValueType):
    display_name = 'Energy'

class Joule(Unit):
    value_type = Energy
    display_name = 'Joule'
    short_name = 'J'

class Calorie(Unit):
    value_type = Energy
    display_name = 'Calorie'
    short_name = 'cal'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value*Fraction('0.238846')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value/Fraction('0.238846')

class Electronvolt(Unit):
    value_type = Energy
    display_name = 'Electronvolt'
    short_name = 'eV'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value*(Fraction('0.62415')*(Fraction('10')**19))

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value/(Fraction('0.62415')*(Fraction('10')**19))

class Kilowatthour(Unit):
    value_type = Energy
    display_name = 'Kilowatt hour'
    short_name = 'kWh'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value*(Fraction('1')/Fraction('3600000'))

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value/(Fraction('1')/Fraction('3600000'))