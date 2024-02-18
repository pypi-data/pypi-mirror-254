import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def dummy(
    obj=None,
    getorfromdummy=1,
    prefix=None,
    prefix_sep="_",
    sep=None
    ):
    """
    这是一个变量虚拟化的文档字符串。

    参数:
    obj (Series or DataFrame): dataframe或者series对象。
    getorfromdummy (binary): 是否生成哑变量{1,0}，1表示生成哑变量，0表示从哑变量还原变量。
    prefix (str): 生成哑变量时的列名前缀。
    prefix_sep (str): 生成哑变量时的列名中的分隔符。
    sep (str): 还原哑变量的指定分隔符。

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../dummy.py", "rt", encoding="utf8") as fp: exec(fp.read())
    ===============================================================================1
    测试还原哑变量
    >>> df = pd.DataFrame({"a": [1, 0, 0, 1], "b": [0, 1, 0, 0], "c": [0, 0, 1, 0]})
    >>> print(df)
    >>> res = dummy(df, getorfromdummy=0)
    >>> print(res)
    ===============================================================================2
    >>> df = pd.DataFrame({"col1_a": [1, 0, 1], "col1_b": [0, 1, 0], "col2_a": [0, 1, 0], "col2_b": [1, 0, 0], "col2_c": [0, 0, 1]})
    >>> print(df)
    >>> res = dummy(df, getorfromdummy=0, sep="_")
    >>> print(res)
    ===============================================================================3
    测试变量虚拟化，给定前缀
    >>> s = pd.Series(list('abca'))
    >>> print(s)
    >>> res = dummy(s, prefix="AA")
    >>> print(res)
    ===============================================================================4
    测试变量虚拟化，给定前缀，给定分隔符
    >>> s = pd.Series(list('abca'))
    >>> print(s)
    >>> res = dummy(s, prefix="AA", prefix_sep="+")
    >>> print(res)
    ===============================================================================5
    """
    if bool(getorfromdummy):
        res = pd.get_dummies(obj, prefix=prefix, prefix_sep=prefix_sep)
        return res
    else:
        res = pd.from_dummies(obj, sep=sep)
        return res
