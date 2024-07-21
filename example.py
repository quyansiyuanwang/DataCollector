from core import AwaitTestTogether

testit = AwaitTestTogether()


@testit(display_kwargs=False)
def add(a, b):
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


@testit(display_doc=False)
def sub(a, b):
    return a - b


@testit
def hello(string):
    return string + ' hello'


@testit
def raise_err():
    1 / int(0.1)


sub(1, 9)
add(3, 1).display_config.display_doc = False
sub(4, 6).display_config["display_args", "display_kwargs"] = True, False
add(114000, 514).display_config.display_doc = False
add(114000, 514).run_config.update({'display_doc': False})
add(1, 2) >> 4  # 1 + 2 = 4
hello('Alex') >> 'Alex hello'
raise_err()


testit.runall(ignore_unexpected=True, ignore_error=True)

print(testit)
# print(testit[sub][0].run(ignore_unexpected=True))
