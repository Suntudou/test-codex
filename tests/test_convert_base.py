import unittest
from src import convert_base

class TestBaseConverter(unittest.TestCase):
    def test_binary_to_decimal(self):
        self.assertEqual(convert_base.convert_base('1010', 2, 10), '10')

    def test_decimal_to_hex(self):
        self.assertEqual(convert_base.convert_base('255', 10, 16), 'FF')

    def test_hex_to_binary(self):
        self.assertEqual(convert_base.convert_base('1F', 16, 2), '11111')

    def test_negative_numbers(self):
        self.assertEqual(convert_base.convert_base('-10', 10, 2), '-1010')

    def test_base_out_of_range(self):
        with self.assertRaises(ValueError):
            convert_base.convert_base('1', 1, 10)

if __name__ == '__main__':
    unittest.main()
