import unittest

from grishina_anastasiia.arab_to_roman_converter.arab_to_roman_converter import ArabToRomanConverter


class ArabToRomanConverterTest(unittest.TestCase):

    def test_class_creating(self):
        self.assertTrue(isinstance(ArabToRomanConverter(1), ArabToRomanConverter))

    def test_convert_arab_one_to_roman(self):
        converter = ArabToRomanConverter(1)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'I')

    def test_convert_arab_two_to_roman(self):
        converter = ArabToRomanConverter(2)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'II')

    def test_convert_arab_five_to_roman(self):
        converter = ArabToRomanConverter(5)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'V')

    def test_convert_arab_ten_to_roman(self):
        converter = ArabToRomanConverter(10)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'X')

    def test_convert_arab_seventy_to_roman(self):
        converter = ArabToRomanConverter(70)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'LXX')

    def test_convert_arab_fifteen_to_roman(self):
        converter = ArabToRomanConverter(15)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'XV')

    def test_convert_arab_eighty_two_to_roman(self):
        converter = ArabToRomanConverter(82)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'LXXXII')

    def test_convert_arab_hundred_to_roman(self):
        converter = ArabToRomanConverter(100)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'C')

    def test_convert_arab_150_to_roman(self):
        converter = ArabToRomanConverter(150)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'CL')

    def test_convert_arab_288_to_roman(self):
        converter = ArabToRomanConverter(288)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'CCLXXXVIII')

    def test_convert_arab_1000_to_roman(self):
        converter = ArabToRomanConverter(1000)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'M')

    def test_convert_arab_5000_to_roman(self):
        converter = ArabToRomanConverter(5000)
        self.assertEqual(converter.convert_arab_to_roman_number(), 'MMMMM')


class RomanToArabConverterTest(unittest.TestCase):

    def test_convert_roman_one_to_arab(self):
        converter = ArabToRomanConverter('I')
        self.assertEqual(converter.convert_roman_to_arab_number(), 1)

    def test_convert_roman_5_to_arab(self):
        converter = ArabToRomanConverter('V')
        self.assertEqual(converter.convert_roman_to_arab_number(), 5)

    def test_convert_roman_4_to_arab(self):
        converter = ArabToRomanConverter('IV')
        self.assertEqual(converter.convert_roman_to_arab_number(), 4)

    def test_convert_roman_6_to_arab(self):
        converter = ArabToRomanConverter('VI')
        self.assertEqual(converter.convert_roman_to_arab_number(), 6)

    def test_convert_roman_9_to_arab(self):
        converter = ArabToRomanConverter('IX')
        self.assertEqual(converter.convert_roman_to_arab_number(), 9)

    def test_convert_roman_10_to_arab(self):
        converter = ArabToRomanConverter('X')
        self.assertEqual(converter.convert_roman_to_arab_number(), 10)

    def test_convert_roman_14_to_arab(self):
        converter = ArabToRomanConverter('XIV')
        self.assertEqual(converter.convert_roman_to_arab_number(), 14)

    def test_convert_roman_944_to_arab(self):
        converter = ArabToRomanConverter('CMXLIV')
        self.assertEqual(converter.convert_roman_to_arab_number(), 944)
