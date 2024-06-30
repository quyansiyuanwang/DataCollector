from typing import Union

from utils.ProjectPath import TestTogetherRunResultsPath
from core import *

Digit = Union[int, float]


class TestSimulate:
    @staticmethod
    def test_normalFunctionWithoutKwargs():
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
        def sub(a: Digit, b: Digit) -> Digit:
            return a - b

        add(1, 2)
        sub(1, 2)
        add(3, 1)
        sub(3, 1)

        testit.runall()

        with open(TestTogetherRunResultsPath / "normalFunctionWithoutKwargs", "w") as file:
            file.write(testit.__str__())

    @staticmethod
    def test_normalFunctionWithConfig():
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

        with open(TestTogetherRunResultsPath / "normalFunctionWithConfigResults", "w") as file:
            file.write(testit.__str__())

    @staticmethod
    def test_normalFunctionWithKwargs():
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

        with open(TestTogetherRunResultsPath / "normalFunctionWithKwargs", "w") as file:
            file.write(testit.__str__())

        print(testit.__str__())

    @staticmethod
    def test_normalFunctionSingleConfig():
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

        with open(TestTogetherRunResultsPath / "normalFunctionSingleConfig", "w") as file:
            file.write(testit.__str__())

        print(testit.__str__())

    @staticmethod
    def test_normalFunctionObjGlobalConfig():
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

        with open(TestTogetherRunResultsPath / "normalFunctionObjGlobalConfig", "w") as file:
            file.write(testit.__str__())

        print(testit.__str__())

    @staticmethod
    def test_normalFunctionGetitemMethod():
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

        print(testit[sub][1].run(ignore_unexpected=True))

        with open(TestTogetherRunResultsPath / "normalFunctionGetitemMethod_SingleFunc", "w") as file:
            file.write(testit[add].__str__())
        print(testit[add].__str__())

        with open(TestTogetherRunResultsPath / "normalFunctionGetitemMethod_SingleStrKey", "w") as file:
            file.write(testit["args"].__str__())
        print(testit["args"].__str__())

        with open(TestTogetherRunResultsPath / "normalFunctionGetitemMethod_StrKeys", "w") as file:
            file.write(testit["args", "result"].__str__())
        print(testit["args", "result"].__str__())


def temp_simulation():
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
    def sub(a: Digit, b: Digit) -> Digit:
        return a - b

    add(1, 2).display_config["display_args"] = False
    sub(1, 2)
    add(3, 1)
    sub(3, 1)

    testit.runall()

    print(testit.__str__())


if __name__ == '__main__':
    # TestSimulate.test_normalFunctionWithoutKwargs()
    # TestSimulate.test_normalFunctionWithConfig()
    # TestSimulate.test_normalFunctionGetitemMethod()
    # TestSimulate.test_normalFunctionWithKwargs()
    # TestSimulate.test_normalFunctionSingleConfig()
    # TestSimulate.test_normalFunctionObjGlobalConfig()
    # temp_simulation()
    pass
