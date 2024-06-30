from copy import deepcopy
from typing import Protocol

from .Configs import DisplayConfig, RunConfig
from .SupportLibs import Gather


class RunResultError(Exception): pass


class _Box(Protocol):
    _id: int


class _RunResult:
    """
    用于内部结果传输与通信
    """
    const_success = "SUCCESS"
    const_failure = "FAILURE"
    const_unexpected = "UNEXPECTED"

    def __init__(self, case=None): self.case = case


class TestBase:
    """
    测试对象基类
    """

    def __init__(
            self,
            func,
            _id,
            display_config=None,
            run_config=None
    ):
        self.func = func
        self._id = _id

        self.display_config = display_config
        self.run_config = run_config

    def __call__(self, *args, **kwargs):
        if self.run_config: return self.func(
            *self.run_config.args, **self.run_config.kwargs
        )
        return self.func(*args, **kwargs)

    def __repr__(self):
        return (f"<Test({self._id})>"
                + " = {{\n"
                  f"{self.run_config}\n"
                  f"{self.display_config}\n"
                  "}}")

    def __eq__(self, other):
        return self._id == other._id

    def __rshift__(self, other):  # 注意： 此`>>`方法用于设置期望值
        self.run_config.expectation = other
        return self.run_config.result == self.run_config.expectation

    """
    以下特殊获取与设置方法
    """

    @property
    def result(self): return self.run_config.result

    @property
    def expectation(self): return self.run_config.expectation

    @expectation.setter
    def expectation(self, value): self.run_config.expectation = value


class Test(TestBase):
    """
    测试对象类
    """

    def __str__(self):
        display_func_name = self.display_config.display_func_name
        display_doc = self.display_config.display_doc
        display_args = self.display_config.display_args
        display_kwargs = self.display_config.display_kwargs
        display_result = self.display_config.display_result
        display_expectation = self.display_config.display_expectation
        doc = remove_excessive_indents(self.func.__doc__) if self.func.__doc__ is not None else "None"

        contents = (
                       f"Function: {self.func.__name__} \n\t" if display_func_name else "") + (
                       f"Doc:\t{doc} \n\t" if display_doc else "") + (
                       f"Args:\t{self.run_config.args} \n\t" if display_args else "") + (
                       f"Kwargs:\t {self.run_config.kwargs} \n\t" if display_kwargs else "") + (
                       f"result:\t {self.run_config.result}\n\t" if display_result else "") + (
                       f"expectation: {self.run_config.expectation}\n" if display_expectation else ""
                   )

        return contents

    def __expect_run(
            self,
            case,
            ignore_unexpected=False,
            ignore_error=False
    ):
        """
        运行函数并判断是否符合期望
        Args:
            case: `_RunResult`类实例化对象, 用于存储运行结果
            ignore_unexpected: 不符期望值是否引发错误
            ignore_error: 忽略函数运行引发的错误

        Returns:
            函数运行结果(result), 运行情况(case)
        """
        try:
            result = self.func(
                *self.run_config.args,
                **self.run_config.kwargs
            )
            case.case = _RunResult.const_success

            if self.expectation != result:
                case.case = _RunResult.const_unexpected
                if not ignore_unexpected: raise RunResultError(
                    f"{self.func.__name__}({self.run_config.args},{self.run_config.kwargs})"
                    f"结果与期望值不符，期望`{self.expectation}`但得到`{result}`: [`{self.expectation} != {result}`]"
                )

        except RunResultError as e:
            result = repr(e)
            if not ignore_unexpected: raise e
            case.case = _RunResult.const_unexpected

        except Exception as e:
            result = repr(e)
            if not ignore_error: raise e
            case.case = _RunResult.const_failure

        return result, case

    def run(self, ignore_unexpected=False, ignore_error=False, _return_case=False):
        """
        运行函数
        Args:
            ignore_unexpected: 不符期望值是否引发错误
            ignore_error: 忽略函数运行引发的错误
            _return_case: 是否返回`case`(`_RunResult`)对象

        Returns:
            如果`_return_case`为`False`, 返回函数运行结果(result)
            如果`_return_case`为`True`, 返回运行情况(case)
        """
        case = _RunResult()

        result, case = self.__expect_run(
            case=case,
            ignore_error=ignore_error,
            ignore_unexpected=ignore_unexpected
        )

        self.run_config.result = result

        return case if _return_case else result


class AwaitTestTogether(Gather):
    def __init__(
            self,
            structure=None,
            default_display_config=None
    ):
        super().__init__(structure if structure is not None else list())
        self.recognize_id = 0
        self.__successes = 0
        self.__failures = 0
        self.__unexpected = 0

        self.display_config = default_display_config
        if self.display_config is None: self.init_display()
        self.add_filter(_Box, Box_filter)

    def init_display(self):
        self.display_config = DisplayConfig(
            _id=self.recognize_id
        )

    def clear(self):
        self.structure = list()

    def __call__(
            self,
            func=None,
            *,
            display_func_name=None,
            display_doc=None,
            display_args=None,
            display_kwargs=None,
            display_result=None
    ):
        self.recognize_id += 1

        uni_config = DisplayConfig(_id=self.recognize_id)
        for cfg_name in self.display_config.attr_constants:
            cfg_v = locals().get(cfg_name, None)
            uni_config[cfg_name] = \
                cfg_v if cfg_v is not None else getattr(self.display_config, cfg_name)

        def inner(function_):
            test = Test(
                func=function_,
                display_config=uni_config,
                _id=self.recognize_id,
                run_config=RunConfig(
                    _id=self.recognize_id
                )
            )

            def decorator(*args, **kwargs):
                new_test = deepcopy(test)
                new_test.run_config.args = args
                new_test.run_config.kwargs = kwargs
                self.structure.append(new_test)
                return new_test

            return TestBase(decorator, _id=self.recognize_id)

        if func is None:
            return TestBase(func=inner, _id=self.recognize_id)

        return TestBase(func=inner(func), _id=self.recognize_id)

    def runall(self, ignore_unexpected=False, ignore_error=False):
        for test in self.structure:
            case = test.run(
                ignore_error=ignore_error,
                ignore_unexpected=ignore_unexpected,
                _return_case=True
            )
            if case.case is _RunResult.const_success:
                self.__successes += 1
            elif case.case is _RunResult.const_failure:
                self.__failures += 1
            elif case.case is _RunResult.const_unexpected:
                self.__unexpected += 1
            else:
                assert False, "built-in error raised!"

        return self

    def __getitem__(self, items):
        items = self._check_dispose_items(items)
        first_item = items[0]
        if hasattr(first_item, '_id'): return AwaitTestTogether(
            super().__getitem__(items)
        )
        return super().__getitem__(items)

    def __len__(self):
        return len(self.structure)

    def __str__(self):
        tests = '\n'.join(
            f"Test{idx + 1}: \n" +
            f"\t{test}\n" for idx, test in enumerate(iterable=self.structure)
        )
        tests_num = f" [{self.__len__()}] Tests here"
        return f"{tests_num:-^60}\n" \
               f"{tests}\n" \
               f"{'ResultCounter':-^60}\n" \
               f"\t total: {self.__len__()}; " \
               f"successes: {self.__successes}; " \
               f"unexpected: {self.__unexpected}; " \
               f"failures: {self.__failures}\n" \
               f"{'-' * 60}\n"


def remove_excessive_indents(doc_string, indent_length=4):
    default_indent = ''.join([" "] * indent_length)
    indent = ""
    lines = doc_string.split('\n')[1:]
    while all(map(
            lambda x: x.startswith(indent), lines
    )) and lines:
        indent += default_indent
    return "\n" + "\n".join(map(lambda x: default_indent * 2 + x[len(indent) - indent_length:], lines))


def Box_filter(one: '_Box', another: '_Box'):
    return getattr(one, '_id') == getattr(another, '_id')
