import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def na(
    obj,
    action="isna",
    fillvalue=None,
    inplace=0,
    bycol=0,
    how="any",
    subset=None,
    method="linear",
    order=None
):
    """
    这是缺失值处理的文档字符串。

    参数:
    obj (Series或者DataFrame): Series或者DataFrame对象。
    action (str): 对缺失值执行的动作{"isna", "notna", "fill", "ffill", "bfill", "delete"}。
    fillvalue (str or numeric): fill动作下的填充值，默认是填充平均值。
    inplace (binary): 是否在原数据上删除缺失值{1,0}。
    bycol (binary): 对DataFrame是否按列指定动作{1,0}。
    how (str): 删除缺失值的方式{"all", "any"}。
    subset (str or list of str): 某些列中含有缺失值才删除对应的行列。
    method (str): 插值算法{"linear", "quadratic", "cubic", "spline", "pchip", "akima", "cubicspline"}。
    order (int): method取值为spline时需要指定的阶数。

    action参数的各个取值的含义如下：
    1. isna: 判断是否为缺失值
    2. notna: 判断是否不为缺失值
    3. bfill: 使用缺失值后面的值（紧邻缺失值的第一个非缺失值）来填充缺失值
    4. ffill: 使用缺失值前面的值（紧邻缺失值的第一个非缺失值）来填充缺失值
    5. fill: 使用给定的值，来填充缺失值
    6. delete: 删除缺失值
    7. interpolate: 插值法填充缺失值

    how参数的各个取值的含义如下：
    1. all: 表示某行列全为缺失值才删除
    2. any: 表示某行列存在缺失值就删除

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../na.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> import numpy as np
    >>> import pandas as pd
    >>> df = pd.DataFrame(np.random.randn(5, 3), index=["a", "c", "e", "f", "h"], columns=["one", "two", "three"])
    >>> df["four"] = "bar"
    >>> df["five"] = df["one"] > 0
    >>> df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
    ===============================================================================1
    DataFrame判断是否为缺失值
    >>> res = na(df2, "isna")
    >>> print(res)
    ===============================================================================2
    Series判断是否为缺失值
    >>> res = na(df2["two"], "isna")
    >>> print(res)
    ===============================================================================3
    DataFrame判断是否不为缺失值
    >>> res = na(df2, "notna")
    >>> print(res)
    ===============================================================================4
    Series判断是否不为缺失值
    >>> res = na(df2["two"], "notna")
    >>> print(res)
    ===============================================================================5
    DataFrame填充缺失值为平均数
    >>> res = na(df2.iloc[:, :3], "fill")
    >>> print(res)
    DataFrame填充缺失值为100
    >>> res = na(df2.iloc[:, :3], "fill", fillvalue=100)
    >>> print(res)
    ===============================================================================6
    Series填充缺失值为平均数
    >>> res = na(df2["two"], "fill")
    >>> print(res)
    Series填充缺失值为100
    >>> res = na(df2["two"], "fill", fillvalue=100)
    >>> print(res)
    Series填充缺失值为foo
    >>> res = na(df2["four"], "fill", fillvalue="foo")
    >>> print(res)
    ===============================================================================7
    DataFrame向前填充
    >>> res = na(df2, "ffill")
    >>> print(res)
    ===============================================================================8
    Series向前填充
    >>> res = na(df2, "ffill")
    >>> print(res)
    Series向前填充
    >>> res = na(df2["four"], "ffill")
    >>> print(res)
    ===============================================================================9
    DataFrame向后填充
    >>> res = na(df2, "ffill")
    >>> print(res)
    ===============================================================================10
    Series向后填充
    >>> res = na(df2, "ffill")
    >>> print(res)
    Series向后填充
    >>> res = na(df2["four"], "ffill")
    >>> print(res)
    ===============================================================================11
    DataFrame删除缺失值，按行删除，只要某行存在缺失值就删除，不原地删除
    >>> res = na(df2, "delete")
    >>> print(df2)
    >>> print(res)
    ===============================================================================12
    DataFrame删除缺失值，按行删除，只要某行存在缺失值就删除，原地删除
    >>> res = na(df2, "delete", inplace=1)
    >>> print(df2)
    >>> print(res)
    ===============================================================================13
    DataFrame删除缺失值，按行删除，某行全为缺失值才删除，不原地删除
    >>> res = na(df2, "delete", how="all")
    >>> print(df2)
    >>> print(res)
    ===============================================================================14
    DataFrame删除缺失值，按行删除，某行全为缺失值才删除，原地删除
    >>> res = na(df2, "delete", how="all", inplace=1)
    >>> print(df2)
    >>> print(res)
    ===============================================================================15
    DataFrame删除缺失值，按行删除，只要two列存在缺失值就删除，不原地删除
    >>> res = na(df2, "delete", subset="two")
    >>> print(df2)
    >>> print(res)
    ===============================================================================16
    DataFrame删除缺失值，按行删除，two列和four列全为缺失值才删除，不原地删除
    >>> res = na(df2, "delete", subset=["two", "four"], how="all")
    >>> print(df2)
    >>> print(res)
    ===============================================================================17
    DataFrame删除缺失值，按列删除，某列全为缺失值才删除，不原地删除
    >>> res = na(df2, "delete", how="all", bycol=1)
    >>> print(df2)
    >>> print(res)
    ===============================================================================18
    DataFrame删除缺失值，按列删除，某列存在缺失值就删除，不原地删除
    >>> res = na(df2, "delete", bycol=1)
    >>> print(df2)
    >>> print(res)
    ===============================================================================19
    DataFrame删除缺失值，按列删除，某列存在缺失值就删除，原地删除
    >>> res = na(df2, "delete", bycol=1, inplace=1)
    >>> print(df2)
    >>> print(res)
    ===============================================================================20
    Series删除缺失值，存在缺失值就删除，不原地删除
    >>> res = na(df2["two"], "delete")
    >>> print(df2["two"])
    >>> print(res)
    ===============================================================================21
    Series删除缺失值，全为缺失值才删除，不原地删除（Series只能按照上面的方式删除，这种方法是无法删除的）
    >>> res = na(df2["two"], "delete", how="all")
    >>> print(df2["two"])
    >>> print(res)
    ===============================================================================22
    Series删除缺失值，存在缺失值就删除，原地删除（DataFrame的列是视图，无法原地删除）
    >>> res = na(df2["two"], "delete", inplace=1)
    >>> print(df2["two"])
    >>> print(res)
    ===============================================================================23
    Series删除缺失值，存在缺失值就删除，原地删除（DataFrame的列是视图，无法原地删除，先复制才能）
    >>> s = df2["two"].copy()
    >>> res = na(s, "delete", inplace=1)
    >>> print(s)
    >>> print(res)
    ===============================================================================24
    """
    if action == "isna":
        res = obj.isna()
        return res
    elif action == "notna":
        res = obj.notna()
        return res
    elif action == "fill":
        res = obj.fillna(
            obj.mean() if fillvalue is None else fillvalue,
            inplace=bool(inplace))
        return res
    elif action == "bfill":
        res = obj.bfill(inplace=bool(inplace))
        return res
    elif action == "ffill":
        res = obj.ffill(inplace=bool(inplace))
        return res
    elif action == "delete":
        if isinstance(obj, pd.DataFrame):
            res = obj.dropna(
                inplace=bool(inplace),
                axis=bycol,
                how=how,
                subset=subset)
        else:
            res = obj.dropna(inplace=bool(inplace), axis=bycol)
        return res
    elif action == "interpolate":
        if order is not None:
            res = obj.interpolate(
                method=method,
                inplace=bool(inplace),
                axis=bycol,
                order=order)
        else:
            res = obj.interpolate(
                method=method,
                inplace=bool(inplace),
                axis=bycol)
        return res
    else:
        print("缺失值处理操作失败！")
