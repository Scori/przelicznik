# coding: utf8
from fractions import Fraction
import typing
from .core import *
from .utils import *
from .prefix import *
from .temperature import *
from .distance import *


value_types = sorted(set(get_all_subclasses(ValueType)), key=lambda x: x.__name__)
prefixes = sorted(set(get_all_subclasses(Prefix)), key=lambda x: float(x.multiplier))
units = sorted(set(get_all_subclasses(Unit)) - set([Prefix, ScaleUnit] + prefixes), key=lambda x: x.__name__)
for vt in value_types:
    vt.units = [u for u in units if u.value_type.compatible_with(vt)]


__ALL__ = locals()


