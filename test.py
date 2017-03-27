# coding: utf8
"""
Module containing all test related code.
"""
import unittest
from units import *
from gui import *


class UnitsTestCase(unittest.TestCase):
    """
    Test container for units library. 
    """
    def test_temperature(self):
        """
        Test temperature conversions. 
        """
        k4 = Kelvin(4)
        self.assertEqual(k4.absolute_value, 4)
        self.assertEqual(k4.convert_to(Kelvin).absolute_value, 4)
        self.assertEqual(k4.convert_to(Celsius).absolute_value, 4)
        self.assertEqual(k4.convert_to(Fahrenheit).absolute_value, 4)
        self.assertEqual(k4.fraction(), Fraction('4'))
        self.assertEqual(k4.convert_to(Kelvin).fraction(), Fraction('4'))
        self.assertEqual(k4.convert_to(Celsius).fraction(), Fraction('-269.15'))
        self.assertEqual(k4.convert_to(Fahrenheit).fraction(), Fraction('-452.47'))
        c4 = Celsius(4)
        self.assertEqual(c4.fraction(), Fraction('4'))
        self.assertEqual(c4.convert_to(Kelvin).fraction(), Fraction('277.15'))
        self.assertEqual(c4.convert_to(Celsius).fraction(), Fraction('4'))
        self.assertEqual(c4.convert_to(Fahrenheit).fraction(), Fraction('39.2'))
        f4 = Fahrenheit(4)
        self.assertEqual(f4.fraction(), Fraction('4'))
        self.assertEqual(f4.convert_to(Kelvin).fraction(), Fraction('46367/180'))
        self.assertEqual(f4.convert_to(Celsius).fraction(), Fraction('-140/9'))
        self.assertEqual(f4.convert_to(Fahrenheit).fraction(), Fraction('4'))

    def test_value_type(self):
        """
        Test Unit.value_type validation.
        """
        k4 = Kelvin(4)
        with self.assertRaises(TypeError):
            k4.convert_to(Meter)
        km4 = Meter(Kelvin)(4)
        self.assertEqual(km4.convert_to(Kelvin(Meter)).fraction(), Fraction('4'))
        self.assertEqual(km4.convert_to(Milli(Kelvin(Meter))).fraction(), Fraction('4000'))

    def test_prefix(self):
        """
        Test Prefix and MultiUnit functionality.
        """
        k4 = Kelvin(4)
        self.assertEqual(k4.convert_to(Milli(Kelvin)).absolute_value, Fraction('4'))
        self.assertEqual(k4.convert_to(Milli(Kelvin)).fraction(), Fraction('4000'))
        self.assertEqual(k4.convert_to(Milli(Celsius)).fraction(), Fraction('-269150'))
        c4 = Celsius(4)
        self.assertEqual(c4.convert_to(Mega(Celsius)).absolute_value, Fraction('277.15'))
        self.assertEqual(c4.convert_to(Mega(Kelvin)).fraction(), Fraction('0.00027715'))
        self.assertEqual(c4.convert_to(Mega(Celsius)).fraction(), Fraction('0.000004'))
        km4k = Micro(Kelvin)(4000000)
        self.assertEqual(km4k.absolute_value, Fraction('4'))
        self.assertEqual(km4k.convert_to(Milli(Kelvin)).absolute_value, Fraction('4'))
        self.assertEqual(km4k.convert_to(Milli(Kelvin)).fraction(), Fraction('4000'))
        self.assertEqual(km4k.convert_to(Milli(Celsius)).fraction(), Fraction('-269150'))

    def test_f2s(self):
        """
        Test Fraction to str conversion.
        """
        self.assertEqual(fraction_to_str(Fraction('0'), -2), '0')
        self.assertEqual(fraction_to_str(Fraction('0'), -1), '0')
        self.assertEqual(fraction_to_str(Fraction('0'), 0), '0')
        self.assertEqual(fraction_to_str(Fraction('0'), 1), '0')
        self.assertEqual(fraction_to_str(Fraction('0'), 2), '0')

        self.assertEqual(fraction_to_str(Fraction('1234.5678'), -2), '1200')
        self.assertEqual(fraction_to_str(Fraction('1234.5678'), -1), '1230')
        self.assertEqual(fraction_to_str(Fraction('1234.5678'), 0), '1234')
        self.assertEqual(fraction_to_str(Fraction('1234.5678'), 1), '1234.5')
        self.assertEqual(fraction_to_str(Fraction('1234.5678'), 2), '1234.56')
        self.assertEqual(fraction_to_str(Fraction('1234.5678'), 10), '1234.5678')

        self.assertEqual(fraction_to_str(Fraction('10/3'), 10), '3.3333333333')
        self.assertEqual(fraction_to_str(Fraction('123456789/987654321098765432109876543210'), 50), '0.00000000000000000000012499999884843750012814453124')

    def test_gui(self):
        self.assertTrue(Application() is Application())


if __name__ == '__main__':
    unittest.main()
