import unittest
from typing import Union

from utils.ProjectPath import TestTogetherRunResultsPath
from core import AwaitTestTogether

Digit = Union[int, float]


class MainTests(unittest.TestCase):
    def test_normalFunctionWithoutKwargs(self):
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

        add(1, 2)
        sub(1, 2)
        add(3, 1)
        sub(3, 1)

        testit.runall()

        with open(TestTogetherRunResultsPath / "normalFunctionWithoutKwargs", "r") as file:
            expected = file.read()

        self.assertEqual(expected, testit.__str__())

        print(testit.__str__())

    def test_normalFunctionWithKwargs(self):
        testit = AwaitTestTogether()

        @testit(display_doc=False, display_kwargs=False)
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

        add(1, 2)
        sub(1, 2)
        add(3, 1)

        testit.runall()

        with open(TestTogetherRunResultsPath / "normalFunctionWithKwargs", "r") as file:
            expected = file.read()

        self.assertEqual(expected, testit.__str__())

        print(testit.__str__())

    def test_normalFunctionGetitemMethod(self):
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

        @testit
        def hello(string):
            return string + ' hello'

        @testit
        def raise_err():
            1 / int(0.1)

        sub(1, 9) >> -5
        add(3, 1)
        sub(4, 6)
        add(114000, 514)
        add(1, 2) >> 4  # 1 + 2 = 4
        hello('Alex') >> 'Alex hello'
        raise_err()

        testit.runall(ignore_unexpected=True, ignore_error=True)  # 忽略期望值

        self.assertEqual(-2, testit[sub][1].run(ignore_unexpected=True))

        with open(TestTogetherRunResultsPath / "normalFunctionGetitemMethod_SingleFunc", "r") as file:
            exception = file.read()
            self.assertEqual(exception, testit[add].__str__())

        with open(TestTogetherRunResultsPath / "normalFunctionGetitemMethod_SingleStrKey", "r") as file:
            exception = file.read()
            self.assertEqual(exception, testit["args"].__str__())

        with open(TestTogetherRunResultsPath / "normalFunctionGetitemMethod_StrKeys", "r") as file:
            exception = file.read()
            self.assertEqual(exception, testit["args", "result"].__str__())
