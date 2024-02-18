import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def freq2d(
    obj,
    index,
    columns,
    rownames=None, 
    colnames=None, 
    margins=1, 
    margins_name='总计', 
    normalize=0
):
    """
    这是二维或者更高维度的频数统计的文档字符串。

    参数:
    obj (DataFrame): DataFrame对象。
    index (str or list of str): 作为行名的列。
    columns (str or list of str): 作为列名的列。
    rownames (str): 行名名称。
    colnames (str): 列名名称。
    margins (binary): 是否显示边际频数。
    margins_name (str): 边际频数名称。
    normalize (binary): 是否显示频率{1,0}。

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../freq2d.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> df = read("../data/toothgrowth.txt", textfileparamsdict={"sep": "\t"})
    ===============================================================================1
    基本测试
    >>> print(df)
    >>> res = freq2d(df, "supp", "dose")
    >>> print(res)
    ===============================================================================2
    基本测试，给定行列名
    >>> print(df)
    >>> res = freq2d(df, "supp", "dose", rownames="A", colnames="B")
    >>> print(res)
    ===============================================================================3
    基本测试，不显示边际
    >>> print(df)
    >>> res = freq2d(df, "supp", "dose", rownames="A", colnames="B", margins=0)
    >>> print(res)
    ===============================================================================4
    基本测试，修改边际名称
    >>> print(df)
    >>> res = freq2d(df, "supp", "dose", rownames="A", colnames="B", margins_name="边际频数")
    >>> print(res)
    ===============================================================================5
    基本测试，修改边际名称，显示频率
    >>> print(df)
    >>> res = freq2d(df, "supp", "dose", rownames="A", colnames="B", margins_name="边际频数", normalize=1)
    >>> print(res)
    ===============================================================================6
    """
    res = pd.crosstab(index=obj[index], columns=obj[columns], rownames=rownames, colnames=colnames, margins=bool(margins), margins_name=margins_name, normalize=bool(normalize))
    return res
