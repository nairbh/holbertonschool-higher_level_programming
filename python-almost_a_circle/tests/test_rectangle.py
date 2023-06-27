# tests/test_models/test_rectangle.py
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_attributes(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 12)

if __name__ == "__main__":
    unittest.main()

