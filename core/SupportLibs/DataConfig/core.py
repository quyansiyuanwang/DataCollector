class VariableNotMatch(Exception): pass


class Config:
    """
    该类用于配置一个实例化对象可通过`getattr`方法获取存入属性值
    如果常量集中有常量字符以`$`开头, 那么认为该常量为`特殊常量`
    """

    def __init__(
            self,
            attr_constants,
            _id=None
    ):
        self._id = _id
        self.attr_constants = attr_constants  # 配置默认值表

        # if config is not None:
        #     (cfg := {
        #         name: value for name, value in attr_constants.items()
        #     }).update(config)
        #     for idea, value in cfg.items():
        #         setattr(self, idea, value)
        # else:
        #
        self.update(self.attr_constants)

    def update(self, dictionary):
        for name, value in dictionary.items():
            if name.startswith('$'):
                name = name[1:]
            setattr(self, name, value)
        return self

    def setAll(self, value):
        """
        将所有`非特殊常量`赋值
        Args:
            value: 值

        Returns:
            本身
        """
        for name in self.attr_constants:
            if not name.startswith("$"): setattr(self, name, value)
        return self

    def __setitem__(self, keys, values):
        """
        设定属性值, 支持多属性赋值
        - 可将一个值赋给一个或多个属性(全部赋值)
        - 可将多个值赋给多个属性(一对一赋值, 若数量不对应则引发错误)

        Args:
            keys: 属性名称
            values: 属性值

        Returns:
            None
        """
        isSingleValue = isinstance(values, str) or not hasattr(values, "__iter__")
        isString = isinstance(keys, str)
        if isString and not isSingleValue:
            raise VariableNotMatch(
                f"指定了一个属性[{keys}]但赋予多个值[{values}]"
            )

        if isString: keys = (keys,)
        if not isSingleValue:
            if len(keys) != len(values): raise VariableNotMatch(
                f"指定了多个属性[{keys}]但赋予的值数量不匹配[{values}]"
            )
        else:
            values = [values] * len(keys)

        for cfg_name, var in zip(keys, values):
            setattr(self, cfg_name, var)

    def __bool__(self):
        """
        如果`常量字符集`中存在`bool`为`True`的属性,
        则认为该`Config对象`已经被使用, 返回`True`, 否则`False`

        Returns:
            `常量字符集`中是否存在`bool`为`True`的属性
        """
        return any(
            bool(value) for value in (
                getattr(self, name) for name in self.attr_constants
            )
        )

    def __eq__(self, other):
        """
        一一对应`常量字符集`中的属性值是否与另一个`Config`对象一致
        Args:
            other: 另一个`Config`实例

        Returns:
            是否均一致
        """
        return all(
            getattr(self, key_name) == getattr(other, key_name)
            for key_name in self.attr_constants
        )

    def __repr__(self):
        """
        显示方法
        Returns:
            内容(字符串)
        """
        prop = f"<Config(Box_id={self._id})>" + " = {\n"
        for name in self.attr_constants:
            if name.startswith("$"): name = name[1:]
            prop += f"\t{name}: {getattr(self, name)},\n"
        prop = prop[:-2] + "\n}"
        return prop
