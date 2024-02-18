import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def duplicate(
    obj=None,
    action="is",
    subset=None,
    keep="first"
    ):
    """
    这是一个重复值处理的文档字符串。

    参数:
    obj (Series or DataFrame): dataframe或者series对象。
    action (str): 对重复值从的处理动作{"is", "drop"}is表示判断是否为重复值，drop为删除重复值。
    subset (str or list of str): 在给定的列下判断是否为重复值。
    keep (str): 对重复值的判定{"first", "last", False}。
    1. first表示将重复值中的第一个值不标记为重复值，其他都标记为重复值
    2. last表示将重复值中的最后一个值不标记为重复值，其他都标记为重复值
    3. False表示将所有的重复值都标记


    示例:
    ===============================================================================0
    导入模块
    >>> with open("../duplicate.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx")
    ===============================================================================1
    Series标记重复值
    >>> res = duplicate(iris["Sepal.Length"])
    >>> print(res)
    ===============================================================================2
    Series标记重复值，keep=last
    >>> res = duplicate(iris["Sepal.Length"], keep="last")
    >>> print(res)
    ===============================================================================3
    Series标记重复值，keep=False
    >>> res = duplicate(iris["Sepal.Length"], keep=False)
    >>> print(res)
    ===============================================================================4
    DataFrame标记重复值
    >>> res = duplicate(iris)
    >>> print(res)
    ===============================================================================5
    DataFrame标记重复值，指定变量
    >>> res = duplicate(iris, subset="Species")
    >>> print(res)
    ===============================================================================6
    Series删除重复值
    >>> res = duplicate(iris["Sepal.Length"], action="drop")
    >>> print(res)
    ===============================================================================7
    DataFrame删除重复值
    >>> res = duplicate(iris, action="drop", subset="Species")
    >>> print(res)
    ===============================================================================8
    """
    if action  == "is":
        if isinstance(obj, pd.Series):
            res = obj.duplicated(keep=keep)
        elif isinstance(obj, pd.DataFrame):
            res = obj.duplicated(subset=subset, keep=keep)
        else:
            res = None
        return res
    else:
        if isinstance(obj, pd.Series):
            res = obj.drop_duplicates(keep=keep)
        elif isinstance(obj, pd.DataFrame):
            res = obj.drop_duplicates(subset=subset, keep=keep)
        else:
            res = None
        return res
