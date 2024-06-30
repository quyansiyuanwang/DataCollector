from typing import (
    Tuple,
    Any,
    Dict,
    Union,
    List,
    Protocol,
    Type,
    Callable,
    Optional,
    TypeVar)


class _RunResult: ...


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


class RunConfig(Config):
    args: ArgsType
    kwargs: KwargsType
    result: Any
    ...


class DisplayConfig(Config):
    display_func_name: bool
    display_doc: bool
    display_args: bool
    display_kwargs: bool


T = TypeVar('T')
ArgsType = Tuple[Any, ...]
KwargsType = Dict[str, Any]
TupleType = Tuple[Any, ...]
DictType = Dict[str, Any]
ItemsType = Union[
    Tuple[str, ...],
    Test,
    int,
    str,
    T
]
FilterType = Callable[[Any, Any], bool]
FunctionType = Callable[..., Any]
StructureType = List[Union[
    Test,
    TestBase,
    ArgsType,
    KwargsType,
    Config,
    DisplayConfig,
    RunConfig,
    T
]]


class GetItemError(Exception): ...


class Gather:
    structure: StructureType
    filters: Dict[Type, FilterType]

    def __init__(self, structure: StructureType) -> None: ...

    @classmethod
    def _check_dispose_items(cls, items: ItemsType) -> TupleType: ...

    def add_filter(self, type_: Type, new_filter: FilterType) -> None: ...

    def __getitem__(
            self,
            items: ItemsType
    ) -> Union[Gather, Any]:
        first_item: Any
        first_item_type: Type
        isAllSameType: bool
        idx: int
        target_ids: Tuple[int, None, ...]

        def getter(target: Test) -> TupleType:
            res: Tuple[Any]
            ...

        ...

    def __len__(self) -> int: ...

    def __str__(self):
        prop: str

    def __eq__(self, other: "Gather") -> bool: ...
