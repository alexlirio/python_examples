from unittest import TestCase
from example1 import calculator


class Test(TestCase):

    def test_sum(self):
        TestCase.assertTrue(calculator.my_sum(1, 2), 3)

