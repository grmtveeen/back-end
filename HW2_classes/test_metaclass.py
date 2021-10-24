import unittest
from mataclass import CustomClass


class TestCustomClass(unittest.TestCase):
    def setUp(self):
        self.inst1 = CustomClass()
        self.inst2 = CustomClass(257)

    def test_custom_x(self):
        self.assertEqual(self.inst1.custom_x, 50)
        self.assertEqual(self.inst2.custom_x, 50)

    def test_custom_val(self):
        self.assertEqual(self.inst1.custom_val, 99)
        self.assertEqual(self.inst2.custom_val, 257)

    def test_custom_line(self):
        self.assertEqual(self.inst1.custom_line(), 100)
        self.assertEqual(self.inst2.custom_line(), 100)

    def test_x(self):
        with self.assertRaises(AttributeError):
            self.inst1.line
        with self.assertRaises(AttributeError):
            self.inst2.line

    def test_val(self):
        with self.assertRaises(AttributeError):
            self.inst1.val
        with self.assertRaises(AttributeError):
            self.inst2.val

    def test_line(self):
        with self.assertRaises(AttributeError):
            self.inst1.line()
        with self.assertRaises(AttributeError):
            self.inst2.line()
