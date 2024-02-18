import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def group(
    obj,
    by,
    groupname=None,
    func=None,
    renamedict=None,
    **kwargs
):
    """
    这是对数据分组后将函数应用到数据上的文档字符串。

    参数:
    obj (DataFrame): DataFrame对象。
    by (str or list of str): 分组变量名。
    groupname (str or list of str): 组别名，返回分组后的数据。
    renamedict (dict): 对分组聚合列的重命名字典，键为原名称，值为新名称。
    func (str or callalbe or dict or list): 应用的函数。
    str可以的取值有{
        "any",
        "all",
        "count",
        "cov",
        "first",
        "idxmax",
        "idxmin",
        "last",
        "max",
        "min",
        "mean",
        "median",
        "sum",
        "nunique",
        "prod",
        "quantile",
        "sem",
        "size",
        "skew",
        "std",
        "var",
        "bfill",
        "cumsum",
        "cumprod",
        "cummax",
        "cummin",
        "cumcount",
        "diff",
        "ffill",
        "fillna",
        "rank",
        "shift",
        "nth",
        "head",
        "tail"
    }

    示例:
    ===============================================================================0
    导入模块
    >>> import numpy as np
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../group.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx", excelfileparamsdict={"index_col": 0})
    ===============================================================================1
    不给func，只分组
    >>> res = group(iris, by="Species")
    >>> print(res)
    ===============================================================================2
    不给func，只分组，给定组别名称
    >>> res = group(iris, by="Species", groupname="virginica")
    >>> print(res)
    ===============================================================================3
    单变量分组，给定单个func
    >>> res = group(iris, by="Species", func="sum")
    >>> print(res)
    ===============================================================================4
    单变量分组，给定多个func
    >>> res = group(iris, by="Species", func=["mean", "std"])
    >>> print(res)
    ===============================================================================5
    单变量分组，给定多个func，自定义函数
    >>> res = group(iris, by="Species", func=["mean", lambda x: x.max()-x.min()])
    >>> print(res)
    ===============================================================================6
    多变量分组，给定单个func
    >>> df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"], "B": ["one", "one", "two", "three", "two", "two", "one", "three"], "C": np.random.randn(8), "D": np.random.randn(8)})
    >>> print(df)
    >>> res = group(df, by=["A", "B"], func="mean")
    >>> print(res)
    ===============================================================================7
    多变量分组，给定多个func
    >>> df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"], "B": ["one", "one", "two", "three", "two", "two", "one", "three"], "C": np.random.randn(8), "D": np.random.randn(8)})
    >>> print(df)
    >>> res = group(df, by=["A", "B"], func=["mean", "sum", lambda x: x.min()/x.max()])
    >>> print(res)
    ===============================================================================8
    单变量分组，给定单个func，改名称
    >>> res = group(iris, by="Species", func=["sum"], renamedict={"sum": "求和"})
    >>> print(res)
    ===============================================================================9
    单变量分组，给定多个func，改名称
    >>> res = group(iris, by="Species", func=["sum", "mean"], renamedict={"sum": "求和", "mean": "平均值"})
    >>> print(res)
    ===============================================================================10
    多个变量分组，给定一个func，改名称
    >>> df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"], "B": ["one", "one", "two", "three", "two", "two", "one", "three"], "C": np.random.randn(8), "D": np.random.randn(8)})
    >>> print(df)
    >>> res = group(df, by=["A", "B"], func=["mean"], renamedict={"mean": "均值"})
    >>> print(res)
    ===============================================================================11
    多个变量分组，给定多个func，改名称
    >>> df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"], "B": ["one", "one", "two", "three", "two", "two", "one", "three"], "C": np.random.randn(8), "D": np.random.randn(8)})
    >>> print(df)
    >>> res = group(df, by=["A", "B"], func=["sum", "mean"], renamedict={"sum": "求和", "mean": "平均值"})
    >>> print(res)
    ===============================================================================12
    单变量分组，给定func，字典形式
    >>> res = group(iris, by="Species", func={"Sepal.Length": "sum"})
    >>> print(res)
    ===============================================================================13
    单变量分组，给定func，字典形式，改名
    >>> res = group(iris, by="Species", func={"Sepal.Length": "sum"}, renamedict={"sum": "求和"})
    >>> print(res)
    ===============================================================================14
    单变量分组，给定func，字典形式
    >>> res = group(iris, by="Species", func={"Sepal.Length": ["sum", "mean"], "Sepal.Width": ["max", "var"]})
    >>> print(res)
    ===============================================================================15
    单变量分组，给定func，字典形式，改名
    >>> res = group(iris, by="Species", func={"Sepal.Length": ["sum", "mean"], "Sepal.Width": ["mean", "var"]}, renamedict={"sum": "求和", "mean": ["Length均值", "Width均值"], "var": "方差"})
    >>> print(res)
    ===============================================================================16
    单变量分组，给定func，字典形式，改名
    >>> res = group(iris, by="Species", func={"Sepal.Length": "mean", "Sepal.Width": "sum"}, renamedict={"mean": "均值", "sum": "求和"})
    >>> print(res)
    ===============================================================================17
    单变量分组，给定func，字典形式，改名
    >>> res = group(iris, by="Species", func={"Sepal.Length": ["sum", "mean"], "Sepal.Width": "mean"}, renamedict={"sum": "求和", "mean": ["Length均值", "Width均值"]})
    >>> print(res)
    ===============================================================================18
    单变量分组，给定func，字典形式，改名
    >>> res = group(iris, by="Species", func={"Sepal.Length": "mean", "Sepal.Width": "mean"}, renamedict={"mean": ["Length均值", "Width均值"]})
    >>> print(res)
    ===============================================================================19
    """
    grouped = obj.groupby(by=by)
    if groupname is not None:
        res = grouped.get_group(groupname)
        return res
    elif func is not None:
        if renamedict is not None:
            if not isinstance(func, dict):
                res = grouped.agg(func, **kwargs).rename(columns=renamedict)
            else:
                rename_dict = {}
                oldname_lst = []
                columnname_lst = []
                for key, value in func.items():
                    if not isinstance(value, list):
                        oldname_lst.append(value)
                        columnname_lst.append(key)
                    else:
                        oldname_lst = oldname_lst + value
                        columnname_lst = columnname_lst + [key] * len(value)
                newname_lst = []
                for key, value in renamedict.items():
                    if not isinstance(value, list):
                        newname_lst.append(value)
                    else:
                        newname_lst = newname_lst + value
                for col, newname, oldname in zip(
                        columnname_lst, newname_lst, oldname_lst):
                    rename_dict[newname] = pd.NamedAgg(
                        column=col, aggfunc=oldname)
                res = grouped.agg(**rename_dict)
        else:
            res = grouped.agg(func, **kwargs)
        return res
    else:
        lst = []
        for name, group in grouped:
            lst.append((name, group))
        return lst
