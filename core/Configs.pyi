from typing import (
    Union,
    Dict,
    Tuple,
    Any,
    Callable,
    Optional
)

from .SupportLibs import Config

ArgsType = Tuple[Any]
TupleType = Tuple[Any, ...]
DictType = KwargsType = Dict[str, Any]
FunctionType = Callable[..., Any]

DisplayConfigType = Dict[
    Union[
        "display_func_name",
        "display_doc",
        "display_args",
        "display_kwargs",
        "display_result",
        "display_expectation"
    ],
    bool,
]


class DisplayConfigIdeas:
    display_func_name: bool
    display_doc: bool
    display_args: bool
    display_kwargs: bool
    display_result: bool
    display_expectation: bool


class RunConfigIdeas:
    args: ArgsType
    kwargs: KwargsType
    result: Any
    expectation: Any


class Undefined:
    def __eq__(self, other: Any) -> True: ...

    def __bool__(self) -> False: ...

    def __repr__(self) -> str: ...


class DisplayConfig(Config, DisplayConfigIdeas, ...):
    def __init__(
            self,
            config: Optional[DisplayConfigType] = None,
            _id: Optional[int] = None
    ) -> None:
        super().__init__(...)
        ...


class RunConfig(Config, RunConfigIdeas, ...):
    def __init__(
            self,
            config: Optional[dict] = None,
            _id: Optional[int] = None
    ) -> None:
        super().__init__(...)
        ...
