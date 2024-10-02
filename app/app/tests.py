from django.test import SimpleTestCase

from app import Calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = Calc.add(5, 6)
        self.assertEqual(res, 11)