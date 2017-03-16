import unittest
from units import *


class MyTestCase(unittest.TestCase):
    def test_temperature(self):
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
        k4 = Kelvin(4)
        with self.assertRaises(TypeError):
            k4.convert_to(Meter)

    def test_prefix(self):
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


if __name__ == '__main__':
    unittest.main()
