from typing import Callable, Tuple, Any, Dict, Type, Union

ArgsType = TupleType = Tuple[Any, ...]
DictType = KwargsType = Dict[str, Any]
FunctionType = Callable[..., Any]


def get_raises_info(
        f: FunctionType,
        *args: ArgsType,
        **kwargs: KwargsType
) -> Union[Type, Any]: ...
