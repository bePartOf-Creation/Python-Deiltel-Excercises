from unittest import TestCase
from PythonExercises.Chapter2Execercise.binaryToDecimal import binary_to_decimal


class BinaryTest(TestCase):
    def test_binary_to_decimal(self):
        dec = binary_to_decimal(0)
        self.assertEqual(dec, 0)

    def test_binary_to_decimal_1(self):
        dec = binary_to_decimal(1)
        self.assertEqual(dec, 1)

    def test_binary_to_decimal_10(self):
        dec = binary_to_decimal(10)
        self.assertEqual(dec, 2)

    def test_binary_to_decimal_with_string(self):
        with self.assertRaises(TypeError):
            dec = binary_to_decimal("hello")


