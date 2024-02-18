import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def pivot(
    obj=None,
    values=None,
    index=None,
    columns=None,
    aggfunc="mean",
    margin=0,
    margin_name="All"
):
    """
    这是一个数据透视表的文档字符串。

    参数:
    obj (DataFrame): dataframe对象。
    values (str or list of str): 作为聚合值的列变量。
    index (str or list of str): 作为行名的列分类变量。
    columns (str or list of str): 作为列名的列分类变量。
    aggfunc (str or list or dict or callable): 聚合函数。
    margin (binary): 是否添加边际统计量。
    margin_name (str): 边际统计量的名称。
    aggfunc中的str取值可以是：
    1. any
    2. all
    3. count
    4. cov
    5. idxmax
    6. idxmin
    7. last
    8. max
    9. mean
    10. median
    11. min
    12. nunique
    13. prod
    14. quantile
    15. sem
    16. size
    17. skew
    18. std
    19. sum
    20. var

    示例:
    ===============================================================================0
    导入模块
    >>> import pandas as pd
    >>> with open("../pivot.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"], "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"], "C": ["small", "large", "large", "small", "small", "large", "small", "small", "large"], "D": [1, 2, 2, 3, 3, 4, 5, 6, 7], "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
    ===============================================================================1
    给定index, columns和values，单个聚合函数
    >>> print(df)
    >>> res = pivot(df, values='D', index=['A', 'B'], columns=['C'], aggfunc="sum")
    >>> print(res)
    ===============================================================================2
    给定index, 和values，多个聚合函数
    >>> print(df)
    >>> res = pivot(df, values=['D', 'E'], index=['A', 'C'], aggfunc={'D': "mean", 'E': "mean"})
    >>> print(res)
    ===============================================================================3
    不同的列给定不同的聚合函数
    >>> print(df)
    >>> res = pivot(df, values=['D', 'E'], index=['A', 'C'], aggfunc={'D': "mean", 'E': ["min", "max", "mean"]})
    >>> print(res)
    ===============================================================================4
    添加边际统计量
    >>> print(df)
    >>> res = pivot(df, values=['D', 'E'], index=['A', 'C'], aggfunc="var", margin=1)
    >>> print(res)
    ===============================================================================5
    添加边际统计量，给定名称
    >>> print(df)
    >>> res = pivot(df, values=['D', 'E'], index=['A', 'C'], aggfunc="var", margin=1, margin_name="方差")
    >>> print(res)
    ===============================================================================6
    """
    res = pd.pivot_table(
        obj,
        values=values,
        index=index,
        columns=columns,
        aggfunc=aggfunc,
        margins=bool(margin),
        margins_name=margin_name)
    return res
