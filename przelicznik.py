# coding: utf8
from fractions import Fraction
import typing


class ValueType:
    pass


class Unit:
    value_type = ValueType
    display_name = ''
    short_name = ''

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value

    def __init__(self, value: typing.Any, is_absolute=False):
        super(Unit, self).__init__()
        if not is_absolute:
            value = self.to_absolute_value(Fraction(value))
        self.absolute_value = Fraction(value)

    def convert_to(self, unit: 'Unit'):
        if self.value_type != unit.value_type:
            raise TypeError('Incompatible unit type')
        return unit(self.absolute_value, True)

    def __float__(self):
        return float(self.from_absolute_value(self.absolute_value))

    def __str__(self):
        return '{0:.20g}{1}'.format(float(self), self.short_name)

    def __repr__(self):
        return '{0}({1})'.format(type(self).__qualname__, self.absolute_value.__repr__())


class Prefix(Unit):
    display_name = ''
    short_name = ''
    multiplier = Fraction('1')
    unit = Unit

    @classmethod
    def create_unit(cls, unit: Unit):
        return type('{0}{1}'.format(cls.display_name.title(), unit.display_name.title()), (cls, unit), {
            'display_name': '{0} {1}'.format(cls.display_name, unit.display_name),
            'short_name': '{0}{1}'.format(cls.short_name, unit.short_name),
            'unit': unit,
        })

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], type) and issubclass(args[0], Unit):
            return cls.create_unit(args[0])
        # return super(cls).__new__(cls, *args, **kwargs)
        return super().__new__(cls)
        print("NEW", cls, args, kwargs, type(r))

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return cls.unit.from_absolute_value(value) / Fraction(cls.multiplier)

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return cls.unit.to_absolute_value(value * Fraction(cls.multiplier))


class Milli(Prefix):
    display_name = 'Milli'
    short_name = 'm'
    multiplier = Fraction('0.001')


class Micro(Prefix):
    display_name = 'Micro'
    short_name = 'μ'
    multiplier = Fraction('0.000001')


class Nano(Prefix):
    display_name = 'Nano'
    short_name = 'n'
    multiplier = Fraction('0.000000001')


class Pico(Prefix):
    display_name = 'Pico'
    short_name = 'p'
    multiplier = Fraction('0.000000000001')


class Kilo(Prefix):
    display_name = 'Kilo'
    short_name = 'k'
    multiplier = Fraction('1000')


class Mega(Prefix):
    display_name = 'Mega'
    short_name = 'M'
    multiplier = Fraction('1000000')


class Giga(Prefix):
    display_name = 'Giga'
    short_name = 'G'
    multiplier = Fraction('1000000000')


class Tera(Prefix):
    display_name = 'Tera'
    short_name = 'T'
    multiplier = Fraction('100000000000000')


class Temperature(ValueType):
    pass


class Distance(ValueType):
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


class Meter(Unit):
    value_type = Distance
    display_name = "Meter"
    short_name = "m"


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
    print()
    mk = Milli(Kelvin)
    print(K4.convert_to(Milli(Kelvin)))
    print(K4.convert_to(Milli(Kelvin)).convert_to(Kelvin))
    print(C4)
    print(C4.convert_to(Milli(Celsius)))
    print(F4)
    print(F4.convert_to(Pico(Kelvin)))
    print(F4.convert_to(Tera(Kelvin)))


