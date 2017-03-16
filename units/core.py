# coding: utf8
from fractions import Fraction
import typing


class ValueType:
    types = set([])

    @classmethod
    def get_types(cls):
        if cls.types:
            return cls.types
        return set([cls])

    @classmethod
    def compatible_with(cls, value_type):
        return cls.get_types() == value_type.get_types()

    def __new__(cls, *value_types):
        types = cls.get_types()
        for t in value_types:
            types.update(t.get_types())
        types.discard(ValueType)
        if not types:
            return ValueType
        return type(
            ''.join([t.__name__ for t in types]),
            (ValueType, ),
            {'types': types},
        )


class Unit:
    value_type = ValueType
    display_name = ''
    short_name = ''
    units = []

    def __init__(self, value: typing.Any, is_absolute=False):
        super(Unit, self).__init__()
        if not is_absolute:
            value = self.to_absolute_value(Fraction(value))
        self.absolute_value = Fraction(value)

    def convert_to(self, unit) -> 'Unit':
        if not self.value_type.compatible_with(unit.value_type):
            raise TypeError('Incompatible unit type')
        return unit(self.absolute_value, True)

    def fraction(self) -> Fraction:
        return self.from_absolute_value(self.absolute_value)

    def __float__(self) -> float:
        return self.fraction().__float__()

    def __str__(self) -> str:
        return '{0:.10g}{1}'.format(self.__float__(), self.short_name)

    def __repr__(self) -> str:
        return '{0}({1})'.format(type(self).__qualname__, self.absolute_value.__repr__())

    @classmethod
    def create_unit(cls, units):
        return type(
            ''.join([unit.display_name for unit in units]),
            (Unit, ),
            {
                'display_name': ' '.join([unit.display_name for unit in units]),
                'short_name': ''.join([unit.short_name for unit in units]),
                'units': units,
                'value_type': ValueType(*[unit.value_type for unit in units]),
            },
        )

    def __new__(cls, *args, **kwargs):
        if kwargs == {} and args and all([isinstance(arg, type) and issubclass(arg, Unit) for arg in args]):
            return cls.create_unit([cls] + list(args))
        return super(Unit, cls).__new__(cls)

    @classmethod
    def from_absolute_value(cls, value: Fraction) -> Fraction:
        for unit in reversed(cls.units):
            value = unit.from_absolute_value(value)
        return value

    @classmethod
    def to_absolute_value(cls, value: Fraction) -> Fraction:
        for unit in cls.units:
            value = unit.to_absolute_value(value)
        return value


class ScaleUnit(Unit):
    display_name = ''
    short_name = ''
    multiplier = Fraction('1')
    unit = Unit

    @classmethod
    def from_absolute_value(cls, value: Fraction) -> Fraction:
        return value / Fraction(cls.multiplier)

    @classmethod
    def to_absolute_value(cls, value: Fraction) -> Fraction:
        return value * Fraction(cls.multiplier)


