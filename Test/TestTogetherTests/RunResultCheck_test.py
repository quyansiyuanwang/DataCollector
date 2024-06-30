import unittest
from typing import Union

from core import AwaitTestTogether, RunResultError
from utils import get_raises_info

Digit = Union[int, float]


class TestTogetherResultCheckTests(unittest.TestCase):
    def test_normalFunctionResultChecking(self):
        testit = AwaitTestTogether()

        @testit
        def add(a: Digit, b: Digit):
            """
            add two numbers
            :param a: a number
            :type a: digit
            :param b: another number
            :type b: digit
            :return: a + b
            :rtype: digit
            """
            return a + b

        @testit
        def sub(a: Digit, b: Digit):
            return a - b

        add(1, 2) >> 4
        sub(1, 9)
        add(3, 1)
        sub(4, 6)
        add(114000, 514)

        def ra(): testit.runall()

        self.assertRaises(RunResultError, ra)

        print(get_raises_info(ra))

    def test_normalFunctionRun(self):
        testit = AwaitTestTogether()

        @testit
        def add(a: Digit, b: Digit):
            """
            add two numbers
            :param a: a number
            :type a: digit
            :param b: another number
            :type b: digit
            :return: a + b
            :rtype: digit
            """
            return a + b

        @testit
        def sub(a: Digit, b: Digit):
            return a - b

        add(1, 2) >> 4
        sub(1, 9)
        add(3, 1)

        self.assertEqual(-8, testit[sub][0].run())


if __name__ == '__main__':
    unittest.main()
