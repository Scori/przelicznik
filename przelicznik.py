# coding: utf8
from decimal import Decimal


class ValueType:
    pass


class Unit:
    value_type = ValueType
    display_name = None
    short_name = None

    @classmethod
    def from_absolute_value(cls, value: Decimal):
        return value

    @classmethod
    def to_absolute_value(cls, value: Decimal):
        return value

    def __init__(self, value: Decimal, is_absolute=False):
        if not is_absolute:
            value = self.to_absolute_value(Decimal(value))
        self.absolute_value = value

    def convert_to(self, unit):
        if self.value_type != unit.value_type:
            raise TypeError('Incompatible unit type')
        return unit(self.absolute_value, True)

    def __str__(self):
        return "{0}{1}".format(self.from_absolute_value(self.absolute_value), self.short_name)

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__qualname__, self.absolute_value.__repr__())


class Prefix(Unit):
    multiplier = Decimal('1')
    display_name = ''
    short_name = ''

    def __init__(self, unit: Unit):
        self.unit = unit

    @classmethod
    def from_absolute_value(cls, value: Decimal):
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
    def from_absolute_value(cls, value: Decimal):
        return value - Decimal('273.15')

    @classmethod
    def to_absolute_value(cls, value: Decimal):
        return value + Decimal('273.15')


if __name__ == '__main__':
    C4 = Celsius(4)
    print(C4)
    print(C4.convert_to(Celsius))
    print(C4.convert_to(Kelvin))
    K4 = Kelvin(4)
    print(K4)
    print(K4.convert_to(Kelvin))
    print(K4.convert_to(Celsius))



