import unittest
from typing import Union

from core import AwaitTestTogether
from utils.ProjectPath import TestTogetherRunResultsPath


Digit = Union[int, float]


class WithConfigTests(unittest.TestCase):
    def test_normalFunctionWithConfig(self):
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

        testit.display_config['display_doc'] = False

        add(1, 2)

        testit.runall()

        with open(TestTogetherRunResultsPath / "normalFunctionWithConfigResults", "r") as file:
            expected = file.read()

        self.assertEqual(expected, testit.__str__())

        print(testit.__str__())

    def test_normalFunctionSingleConfig(self):
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

        add(1, 2).display_config["display_doc", "display_kwargs"] = False
        sub(1, 2).display_config["display_result"] = False  # type: ignore
        add(3, 1)
        sub(3, 1)

        testit.runall()

        with open(TestTogetherRunResultsPath / "normalFunctionSingleConfig", "r") as file:
            expected = file.read()

        self.assertEqual(expected, testit.__str__())

        print(testit.__str__())

    def test_normalFunctionObjGlobalConfig(self):
        testit = AwaitTestTogether()

        @testit(display_kwargs=False, display_doc=False)
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

        with open(TestTogetherRunResultsPath / "normalFunctionObjGlobalConfig", "r") as file:
            expected = file.read()

        self.assertEqual(expected, testit.__str__())

        print(testit)
