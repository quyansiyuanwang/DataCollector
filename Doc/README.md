## 目录
- [简介](#简介)
- [用法](#用法)
- [注意](#注意)

---

## 简介

    这是一个自定义测试框架
    将函数或方法聚合到一起执行
    并获得一个结构化的结果呈现

### 介绍

    TestTogether is a class that allows you to test multiple functions at once.

### 用法
  - 大致过程
    1. 导入`TestTogether`包
    
    2. 创建实例化的对象
    
    3. 使用实例化装饰器传入要测试的函数
    
    4. 然后调用`runall`方法来运行所有测试。
    
    5. 直接打印实例化对象 或 使用`__getitem__`方法获取结果
  
  - 具体方法
    - `runall`: 该方法运行所有已记录的测试。
                并返回一个实例化对象本身。
    ```python
    from DataCollector import AwaitTestTogether


    testit = AwaitTestTogether()
    
    @testit
    def add(a: 'Digit', b: 'Digit'):
        """
        add two numbers
        :param a: a number
        :type a: digit
        :param b: another number
        :type b: digit
        :return: a + b
        :rtype: digit
        """
        return a + b
    
    @testit
    def sub(a: 'Digit', b: 'Digit'):
        return a - b
    
    add(1, 2)
    sub(1, 2)
    add(3, 1)
    
    testit.runall()
    ```
    
    - `__str__`: 该方法返回一个字符串，
                 包含所有测试的结构化结果。
    
    - `display_config`：全局显示配置字典，可以配置__str__方法的显示。
        它有以下键：
        `display_func_name`，
        `display_doc`，
        `display_args`，
        `display_kwargs`，
        `display_Result`。
    
    - `config_init`: 它使用`True`初始化`display_config`属性中的所有配置
    
    - `clear`: 该方法清除所有测试和结果。
    
    - `__getitem__`: 您可以使用 **_被装饰后的函数对象_** 作为字典来获取运行结果。
                    如果未找到该函数，则返回`None`。

    - `__call__`: 此方法支持了该包的装饰器，
    你可以使用运行实例化对象并单独调整该次运行实例的显示配置。



### 注意

1. 暂无