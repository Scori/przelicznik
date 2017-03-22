# coding: utf8
"""
Module containing ValueType and Unit subclasses associated with distance.
"""
from fractions import Fraction
import typing
from .core import ValueType, Unit


class Distance(ValueType):
    display_name = 'Distance'


class Meter(Unit):
    value_type = Distance
    display_name = "Meter"
    short_name = "m"


class Inch(Unit):
    value_type = Distance
    display_name = "Inch"
    short_name = "in"

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value / Fraction('0.0254')

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value * Fraction('0.0254')


class Foot(Unit):
    value_type = Distance
    display_name = "Foot"
    short_name = "ft"

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value / Fraction("0.3048")

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value * Fraction("0.3048")


class Yard(Unit):
    value_type = Distance
    display_name = "Yard"
    short_name = "yd"

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value / Fraction("0.9144")

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value * Fraction("0.9144")


class Mile(Unit):
    value_type = Distance
    display_name = "Mile"
    short_name = "mi"

    @classmethod
    def from_absolute_value(cls, value: Fraction):
        return value / Fraction("1609.344")

    @classmethod
    def to_absolute_value(cls, value: Fraction):
        return value * Fraction("1609.344")
