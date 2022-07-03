"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """tests the Calc module"""

    def test_add_numbers(self):
        """test add numbers"""
        res = calc.add(5,6)

        self.assertEqual(res,11)
    
    def test_subtract_numbers(self):
        """test subtract numbers"""
        res = calc.subtract(5,55)

        self.assertEqual(res,-50)
