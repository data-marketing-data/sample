#!/usr/bin/env python3
"""
算数計算機のテスト
"""

import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """計算機関数のテストケース"""

    def test_add(self):
        """加算のテスト"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10.5, 2.5), 13.0)

    def test_subtract(self):
        """減算のテスト"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10.5, 2.5), 8.0)

    def test_multiply(self):
        """乗算のテスト"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
        """除算のテスト"""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10.0, 4.0), 2.5)

    def test_divide_by_zero(self):
        """0除算のエラーテスト"""
        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
