from typing import (
    Dict,
    Optional,
    Any,
    List,
    Union
)

ConstantType = Dict[str, ...]
DictType = Dict[str, Any]


class VariableNotMatch(Exception): pass


class Config:
    _id: Optional[int]
    attr_constants: Optional[ConstantType]

    def __init__(
            self,
            attr_constants: ConstantType,
            config: Optional[DictType] = None,
            _id: Optional[int] = None
    ):
        idea: str
        value: Any

    def update(self, dictionary: ConstantType) -> 'Config': ...

    def setAll(self, value: Optional[Any]) -> 'Config':
        self
        name: str

    def __setitem__(self, keys, values):
        isSingleValue: bool
        isString: bool
        values: Union[List[Any], Any]
        cfg_name: str
        var: Any
        ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: 'Config') -> bool: ...

    def __repr__(self) -> str:
        prop: str
        name: str
        ...
