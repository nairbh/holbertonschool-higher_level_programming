#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        self.assertEqual(max_integer([1, 5, 2]), 5)
        self.assertEqual(max_integer([5, 2, 3]), 5)
        self.assertEqual(max_integer([-1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
