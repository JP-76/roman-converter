import unittest
from src.roman_converter import integer_to_roman

class TestIntegerToRoman(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(integer_to_roman(1), "I")
        self.assertEqual(integer_to_roman(5), "V")
        self.assertEqual(integer_to_roman(10), "X")
    
    def test_composite_numbers(self):
        self.assertEqual(integer_to_roman(9), "IX")
        self.assertEqual(integer_to_roman(15), "XV")
        self.assertEqual(integer_to_roman(39), "XXXIX")
        self.assertEqual(integer_to_roman(44), "XLIV")
        self.assertEqual(integer_to_roman(99), "XCIX")
        self.assertEqual(integer_to_roman(3999), "MMMCMXCIX")
