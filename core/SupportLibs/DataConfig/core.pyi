from typing import (
    Dict,
    Optional,
    Any
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
    ): ...

    def update(self, dictionary: ConstantType) -> 'Config': ...

    def setAll(self, value: Optional[Any]) -> 'Config': ...

    def __setitem__(self, keys, values): ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: 'Config') -> bool: ...

    def __repr__(self) -> str: ...
