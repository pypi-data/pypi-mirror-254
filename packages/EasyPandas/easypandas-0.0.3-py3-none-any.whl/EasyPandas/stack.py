import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def stack(
    obj,
    isstack=1,
    level=-1,
):
    """
    这是列名和行名转换的文档字符串。

    参数:
    obj (Series or DataFrame): Series对象或者DataFrame对象。
    isstack (binary): 是否将列名转为行名{1,0}1表示将列名转为行名，0表示行名转为列名。
    level (int): 列名转为第几个行名，将第几个行名转为列名。

    示例:
    ===============================================================================0
    导入模块
    >>> import numpy as np
    >>> import pandas as pd
    >>> with open("../stack.py", "rt", encoding="utf8") as fp: exec(fp.read())
    ===============================================================================1
    测试stack参数
    >>> df_single_level_cols = pd.DataFrame([[0, 1], [2, 3]], index=['cat', 'dog'], columns=['weight', 'height'])
    >>> print(df_single_level_cols)
    >>> res = stack(df_single_level_cols)
    >>> print(res)
    ===============================================================================2
    测试unstack参数
    >>> index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'), ('two', 'a'), ('two', 'b')])
    >>> s = pd.Series(np.arange(1.0, 5.0), index=index)
    >>> print(s)
    >>> res = stack(s, isstack=0)
    >>> print(res)
    ===============================================================================3
    测试unstack参数，指定level
    >>> index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'), ('two', 'a'), ('two', 'b')])
    >>> s = pd.Series(np.arange(1.0, 5.0), index=index)
    >>> print(s)
    >>> res = stack(s, isstack=0, level=0)
    >>> print(res)
    ===============================================================================4
    """
    if bool(isstack):
        res = obj.stack(level=level, future_stack=True)
    else:
        res = obj.unstack(level=level)
    return res
