from typing import Final, Any, Dict

from .SupportLibs import Config


class Undefined:
    """
    用于临时赋值
    """

    def __eq__(self, other): return True

    def __bool__(self): return False

    def __repr__(self): return "Undefined<None>"


RUN_CONFIG_DEFAULTS: Final[
    Dict[str, Any]
] = {
    "args": None,
    "kwargs": None,
    "result": Undefined(),
    "$expectation": Undefined()
}

DISPLAY_CONFIG_DEFAULTS: Final[
    Dict[str, Any]
] = {
    "display_func_name": True,
    "display_doc": True,
    "display_args": True,
    "display_kwargs": True,
    "display_result": True,
    "display_expectation": True
}


class DisplayConfig(Config):
    """
    显示配置类
    """

    def __init__(self, _id=None):
        super().__init__(
            _id=_id,
            attr_constants=DISPLAY_CONFIG_DEFAULTS
        )


class RunConfig(Config):
    """
    运行配置类
    """

    def __init__(self, _id=None):
        super().__init__(
            _id=_id,
            attr_constants=RUN_CONFIG_DEFAULTS
        )
        self.expectation = Undefined()
