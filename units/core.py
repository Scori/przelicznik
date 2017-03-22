# coding: utf8
"""
Core module for units package. Defines base classes like ValueType and Unit and utility class ScaleUnit. 
"""
from fractions import Fraction
from collections import Counter
from .utils import fraction_to_str
import typing


class ValueType:
    """
    Abstract class representing type of value. 
    """
    display_name = ''
    types = Counter([])
    units = []

    @classmethod
    def get_types(cls) -> Counter:
        """
        Returns Counter object containing all base value type classes - representation of whole type. 
        """
        if cls.types:
            return cls.types
        return Counter([cls])

    @classmethod
    def compatible_with(cls, value_type: typing.TypeVar('ValueType')) -> bool:
        """
        Check if given *value_type* class is equivalent with *self*. 
        """
        return cls.get_types() == value_type.get_types()

    def __new__(cls, *value_types):
        """
        Create new ValueType subclass representing product of cls and all given *value_types* 
        """
        types = cls.get_types()
        for t in value_types:
            types.update(t.get_types())
        types.pop(ValueType, None)
        if not types:
            return ValueType
        return type(
            ''.join([t.__name__ * k for t, k in types.items()]),
            (ValueType, ),
            {
                'types': types,
                'display_name': ''.join([t.display_name for t, k in types.items() for _ in range(k)])
             },
        )


class Unit:
    """
    Class representing unit of given *value_type*. Instances of this class represent not only unit but also its value.
    """
    value_type = ValueType
    display_name = ''
    short_name = ''
    units = []

    def __init__(self, value: typing.Any, is_absolute=False):
        """
        Initialize unit with given value.  
        """
        super(Unit, self).__init__()
        if not is_absolute:
            value = self.to_absolute_value(Fraction(value))
        self.absolute_value = Fraction(value)

    def convert_to(self, unit: typing.TypeVar('Unit')) -> 'Unit':
        """
        Returns new Unit instance representing current value in given *unit*.
        """
        if not self.value_type.compatible_with(unit.value_type):
            raise TypeError('Incompatible unit type')
        return unit(self.absolute_value, True)

    def fraction(self) -> Fraction:
        """
        Get fraction representation of current value. 
        """
        return self.from_absolute_value(self.absolute_value)

    def smart_str(self, precision=5):
        """
        Get str representation of current value with given *precision*.
        """
        return fraction_to_str(self.fraction(),  precision)

    def __float__(self) -> float:
        """
        Get float representation of current value. 
        """
        return self.fraction().__float__()

    def __str__(self) -> str:
        """
        Get str representation of current value with unit short_name.
        """
        return '{0}{1}'.format(self.smart_str(), self.short_name)

    def __repr__(self) -> str:
        """
        Get Python-valid representation of self. 
        """
        return '{0}({1})'.format(type(self).__qualname__, self.absolute_value.__repr__())

    @classmethod
    def create_unit(cls, units):
        """
        Create new Unit subclass representing product of given units.
        """
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

    def __new__(cls, *args, **kwargs) -> typing.TypeVar('Unit'):
        """
        If Unit subclasses are passed, returns new Unit subclass representing product of cls and all given units.
        In other case instantiates cls and initialises it with passed value.  
        """
        if kwargs == {} and args and all([isinstance(arg, type) and issubclass(arg, Unit) for arg in args]):
            return cls.create_unit([cls] + list(args))
        return super(Unit, cls).__new__(cls)

    def __call__(self, *args, **kwargs) -> 'Unit':
        """
        Not implemented.
        """
        raise NotImplemented

    @classmethod
    def from_absolute_value(cls, value: Fraction) -> Fraction:
        """
        Converts from absolute value to value in this unit.
        """
        for unit in reversed(cls.units):
            value = unit.from_absolute_value(value)
        return value

    @classmethod
    def to_absolute_value(cls, value: Fraction) -> Fraction:
        """
        Converts from value in this unit to absolute value.
        """
        for unit in cls.units:
            value = unit.to_absolute_value(value)
        return value


class ScaleUnit(Unit):
    """
    Utility class providing scaling functionality. 
    """
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


