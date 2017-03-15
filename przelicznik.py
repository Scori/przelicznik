# coding: utf8
from fractions import Fraction

class ValueType:
    pass


class Unit:
    value_type = ValueType
    display_name = None
    short_name = None

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value

    def __init__(self, value: Fraction, is_absolute=False):
        if not is_absolute:
            value = self.to_absolute_value(Fraction(value))
        self.absolute_value = value

    def convert_to(self, unit):
        if self.value_type != unit.value_type:
            raise TypeError('Incompatible unit type')
        return unit(self.absolute_value, True)

    def __str__(self):
        return "{0:.4f}{1}".format(float(self.from_absolute_value(self.absolute_value)), self.short_name)

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__qualname__, self.absolute_value.__repr__())


class Prefix(Unit):
    multiplier = Fraction('1')
    display_name = ''
    short_name = ''

    def __init__(self, unit: Unit):
        self.unit = unit

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value * cls.multiplier


class Temperature(ValueType):
    pass


class Kelvin(Unit):
    value_type = Temperature
    display_name = "Kelvin"
    short_name = '°K'


class Celsius(Unit):
    value_type = Temperature
    display_name = "Celsius"
    short_name = '°C'

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value - Fraction('273.15')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value + Fraction('273.15')

class Fahrenheit(Unit):
    value_type = Temperature
    display_name = "Fahrenheit"
    short_name = "°F"

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return Fraction('32') + Fraction('1.8') * (value - Fraction('273.15'))

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return Fraction('5/9') * (value - Fraction('32')) + Fraction('273.15')


if __name__ == '__main__':
    Fraction(5)
    C4 = Celsius(4)
    print(C4)
    print(C4.convert_to(Celsius))
    print(C4.convert_to(Kelvin))
    print(C4.convert_to(Fahrenheit))
    print()
    K4 = Kelvin(4)
    print(K4)
    print(K4.convert_to(Kelvin))
    print(K4.convert_to(Celsius))
    print(K4.convert_to(Fahrenheit))
    print()
    F4 = Fahrenheit(4)
    print(F4)
    print(F4.convert_to(Celsius))
    print(F4.convert_to(Kelvin))
    print(F4.convert_to(Fahrenheit))

