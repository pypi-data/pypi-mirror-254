import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def cut(
    obj,
    bins,
    cutbyquantile=0,
    labels=None,
    right=1,
    include_lowest=0
):
    """
    这是变量分组的文档字符串。

    参数:
    obj (Series): Series对象。
    bins (int or list of float): 等距分组的组数或者是不等距分组的区间分割点构成的列表或者是分位数点构成的列表。
    cutbyquantile (binary): 是否按照分位数来分组{1,0}。
    labels (list): 分组标签。
    right (binary): 区间的右端点是否封闭{1,0}。
    include_lowest (binary): 第一个区间的左端点是否封闭{1,0}。

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../cut.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx")
    >>> sepal_length = iris["Sepal.Length"]
    ===============================================================================1
    变量等距分组
    >>> res = cut(sepal_length, bins=5)
    >>> print(res)
    ===============================================================================2
    变量不等距分组
    >>> res = cut(sepal_length, bins=[4, 5.5, 6.5, 7, 8])
    >>> print(res)
    ===============================================================================3
    变量不等距分组，给定标签
    >>> res = cut(sepal_length, bins=[4, 6.5, 7.5, 8], labels=["低", "中", "高"])
    >>> print(res)
    ===============================================================================4
    变量不等距分组，给定标签，不包括右边
    >>> res = cut(sepal_length, bins=[4, 6.5, 7.5, 8], right=0)
    >>> print(res)
    ===============================================================================5
    变量不等距分组，给定标签，第一个区间包括左边端点
    >>> res = cut(sepal_length, bins=[4, 6.5, 7.5, 8], include_lowest=1)
    >>> print(res)
    ===============================================================================6
    变量分位数分组
    >>> res = cut(sepal_length, cutbyquantile=1, bins=[0, 0.1, 0.5, 0.9, 1])
    >>> print(res)
    ===============================================================================7
    变量分位数分组，指定标签
    >>> res = cut(sepal_length, cutbyquantile=1, bins=[0, 0.1, 0.5, 0.9, 1], labels=["低", "中低", "中高", "高"])
    >>> print(res)
    ===============================================================================8
    """
    if bool(cutbyquantile):
        res = pd.qcut(obj, bins, labels=labels)
    else:
        res = pd.cut(obj, bins, labels=labels, right=bool(
            right), include_lowest=bool(include_lowest))
    return res
