from typing import (
    Any,
    List,
    Dict,
    Callable,
    Tuple,
    Union,
    Protocol,
    Optional,
    Final, runtime_checkable
)

from .Configs import (DisplayConfig, RunConfig)
from .SupportLibs import Gather

@runtime_checkable
class _Box(Protocol):
    _id: int


class TestBase(_Box):
    func: FunctionType
    _id: int
    display_config: Optional[DisplayConfig]
    run_config: Optional[RunConfig]
    result: Any
    expectation: Any

    def __init__(
            self,
            func: FunctionType,
            _id: int,
            display_config: Optional[DisplayConfig] = None,
            run_config: Optional[RunConfig] = None
    ) -> None: ...

    def __call__(self, *args: ArgsType, **kwargs: KwargsType) -> Any: ...

    def __repr__(self) -> str: ...

    def __eq__(self, other: 'TestBase') -> bool: ...

    # 注意： 此`>>`方法用于设置期望值
    def __rshift__(self, other: Any) -> bool: ...


class Test(TestBase):
    run_config: ...
    func: ...
    display_config: ...
    ...

    def __expect_run(
            self,
            case: _RunResult,
            ignore_unexpected: bool = False,
            ignore_error: bool = False
    ): ...

    def run(
            self,
            ignore_unexpected: bool = False,
            ignore_error: bool = False,
            _return_case: bool = False
    ) -> Union[_RunResult, Any]: ...

    def __str__(self) -> str: ...


class Config:
    _id: int
    attr_constants: List[str]
    config: Dict[str, Any]
    init_value: Any
    ...


ArgsType = TupleType = Tuple[Any, ...]
DictType = KwargsType = Dict[str, Any]
FunctionType = Callable[[...], Any]
StructureType = List[Union[
    TestBase,
    Test,
    ArgsType,
    KwargsType,
    Config,
    DisplayConfig,
    RunConfig
]]


class RunResultError(Exception): pass


class _RunResult:
    const_success: Final[str] = "SUCCESS"
    const_failure: Final[str] = "FAILURE"
    const_unexpected: Final[str] = "UNEXPECTED"

    def __init__(
            self,
            case: Optional[Union[
                const_failure,
                const_success,
                const_unexpected
            ]] = None
    ): ...


TestListType = List[TestBase]

AwaitTestTogetherDecoratorType = Callable[
    [
        Tuple[ArgsType],
        Dict[str, KwargsType]
    ],
    Test
]


class AwaitTestTogether(Gather):
    recognize_id: int
    run_directly: bool
    display_config: Optional[DisplayConfig]
    __failures: int
    __successes: int
    __unexpected: int

    def __init__(
            self,
            structure: Optional[StructureType] = None,
            default_display_config: Optional[DisplayConfig] = None,
            run_directly: bool = False
    ) -> None:
        super().__init__(...)

    def init_display(self) -> None: ...

    def clear(self) -> None: ...

    def __call__(
            self,
            func: FunctionType = None,
            *,
            display_func_name: Optional[bool] = None,
            display_doc: Optional[bool] = None,
            display_args: Optional[bool] = None,
            display_kwargs: Optional[bool] = None,
            display_result: Optional[bool] = None
    ) -> Test:
        uni_config: DisplayConfig
        cfg_v: Optional[bool]

        def inner(function_: FunctionType) -> AwaitTestTogetherDecoratorType:
            def decorator(*args: ArgsType, **kwargs: KwargsType) -> Test: ...

    def runall(self, ignore_unexpected: bool = False, ignore_error: bool = False) -> 'Test': ...

    def __getitem__(self, items: Union[Any, Tuple[Any, ...]]) -> Union[Gather, 'AwaitTestTogether']: ...

    def __len__(self) -> str: ...

    def __str__(self) -> str: ...


def remove_excessive_indents(doc_string: str, indent_length: int = 4) -> str: ...


def Box_filter(one: '_Box', another: '_Box') -> bool: ...
