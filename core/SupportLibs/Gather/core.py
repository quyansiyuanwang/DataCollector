class GetItemError(Exception): pass


class Gather:
    """
    该类用于将同类对象打包，
    并且支持getitem方法获取内容
    """

    def __init__(self, structure):
        self.structure = structure
        self.filters = dict()

    @classmethod
    def _check_dispose_items(cls, items):
        """
        检查并返回`items`对象:
        - 如果`items`为非元组对象, 则将此对象放入元组
        - 如果`items`中的对象类型不同则引发错误
        Args:
            items: 对象(单个或多个)

        Returns:
            元组
        """
        if not isinstance(items, tuple): items = (items,)
        first_item_type = type(items[0])

        isAllSameType = all(isinstance(item, first_item_type) for item in items)
        if not isAllSameType: raise GetItemError(
            f"获取的对象类型不同[{items}]"
        )
        return items

    def add_filter(self, type_, new_filter):
        self.filters.update({type_: new_filter})

    def __getitem__(self, items):
        """
        获取目标对象
        Args:
            items: 目标特征

        Returns:
            包含对象的该类实例化对象
        """
        items = self._check_dispose_items(items)
        first_item = items[0]

        # 自定义筛选器筛选
        for ty, f in self.filters.items():
            if isinstance(first_item, ty): break
        else:
            ty = None

        if ty is not None:
            def filter_(i): return any(f(i, item) for item in items)

            return Gather(list(
                item for item in self.structure if filter_(item)
            ))

        # 基础的工厂处理模式(Factory)
        # 获取单个或多个对象
        if isinstance(first_item, int):
            res = list(self.structure[idx] for idx in items)
            return Gather(res) if len(res) > 1 else res[0]

        elif isinstance(first_item, str):
            def getter(target):
                res_ = tuple(
                    getattr(target.run_config, key) for key in items
                )
                return res_ if len(items) > 1 else res_[0]

            return Gather(
                list(getter(target) for target in self.structure)
            )

        else:
            assert False, GetItemError(
                f"未知的获取对象格式[{items}]"
            )

    def __len__(self):
        return len(self.structure)

    def __iter__(self):
        return self.structure.__iter__()

    def __str__(self):
        prop = "Gather:\n\t"
        for item in self.structure:
            prop += repr(item) + "\n\t"

        return prop[:-1]

    def __eq__(self, other):
        """
        比较等于方法
        Args:
            other: 其他`Gather`实例对象

        Returns:
            是否相等
        """
        return self.structure == other.structure
