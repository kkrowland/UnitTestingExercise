import unittest

class MyTestCase(unittest.TestCase):

    def test_function_name(self):

        result = 2 + 2

        self.assertEqual(result, 4)