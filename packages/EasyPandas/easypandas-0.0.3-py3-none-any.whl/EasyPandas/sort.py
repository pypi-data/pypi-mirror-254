import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def sort(
        df,
        by=None,
        isincreasing=1,
        isinplace=0,
        isreindex=0,
        issortcol=0):
    """
    这是一个对数据排序的函数帮助文档。

    参数:
    df (DataFrame or Series): DataFrame对象或者Series对象。
    by (str or list of str): 按照什么排序，列名或者索引{"index", colname}。
    isincreasing (binary or list of binary): 是否升序排列{1,0}。
    isinplace (binary): 是否在原数据上修改{1,0}。
    isreindex (binary): 是否将排序后的索引设置为0,1,2,...n{1,0}。
    howtosort (callale): 排序方式，可调函数。
    issortcol (binary): 是否对列名进行排序。

    示例:
    ===============================================================================0
    导入模块
    >>> import numpy as np
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../sort.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.csv")
    ===============================================================================1
    对DataFrame按照index排序
    >>> idx = iris.index.tolist()
    >>> np.random.shuffle(idx)
    >>> iris.index = idx
    >>> sortdf = sort(iris, by="index")
    >>> print(sortdf)
    ===============================================================================2
    对DataFrame按照index排序，降序
    >>> idx = iris.index.tolist()
    >>> np.random.shuffle(idx)
    >>> iris.index = idx
    >>> sortdf = sort(iris, by="index", isincreasing=0)
    >>> print(sortdf)
    ===============================================================================3
    对DataFrame按照index排序，重新设置index
    >>> idx = iris.index.tolist()
    >>> np.random.shuffle(idx)
    >>> iris.index = idx
    >>> sortdf = sort(iris, by="index", isincreasing=0, isreindex=1)
    >>> print(sortdf)
    ===============================================================================4
    对DataFrame按照index排序，重新设置index，在原数据上修改
    >>> idx = iris.index.tolist()
    >>> np.random.shuffle(idx)
    >>> iris.index = idx
    >>> sortdf = sort(iris, by="index", isincreasing=0, isreindex=1, isinplace=1)
    >>> print(sortdf)
    >>> print(iris)
    ===============================================================================5
    对DataFrame按照colname排序
    >>> sortdf = sort(iris, by="Sepal.Length")
    >>> print(sortdf)
    ===============================================================================6
    对DataFrame按照colname排序，降序
    >>> sortdf = sort(iris, by="Sepal.Length", isincreasing=0)
    >>> print(sortdf)
    ===============================================================================7
    对DataFrame按照colname排序，重新设置index
    >>> sortdf = sort(iris, by="Sepal.Length", isincreasing=0, isreindex=1)
    >>> print(sortdf)
    ===============================================================================8
    对DataFrame按照colname排序，重新设置index，在原数据上修改
    >>> sortdf = sort(iris, by="Sepal.Length", isincreasing=0, isreindex=1, isinplace=1)
    >>> print(sortdf)
    >>> print(iris)
    ===============================================================================9
    对DataFrame按照多个colname排序
    >>> sortdf = sort(iris, by=["Sepal.Width", "Sepal.Length"])
    >>> print(sortdf)
    ===============================================================================10
    对DataFrame按照多个colname排序，一个升序，一个降序
    >>> sortdf = sort(iris, by=["Sepal.Width", "Sepal.Length"], isincreasing=[1,0])
    >>> print(sortdf)
    ===============================================================================11
    对DataFrame按照多个colname排序，一个升序，一个降序，一个升序，一个降序
    >>> sortdf = sort(iris, by=["Sepal.Width", "Sepal.Length", "Petal.Length", "Petal.Width"], isincreasing=[1,0,1,0])
    >>> print(sortdf)
    ===============================================================================12
    对Series按照index排序
    >>> idx = iris.index.tolist()
    >>> np.random.shuffle(idx)
    >>> iris.index = idx
    >>> sortdf = sort(iris["Sepal.Length"], by="index")
    >>> print(sortdf)
    ===============================================================================13
    对Series按照index排序，降序
    >>> idx = iris.index.tolist()
    >>> np.random.shuffle(idx)
    >>> iris.index = idx
    >>> sortdf = sort(iris["Sepal.Length"], by="index", isincreasing=0)
    >>> print(sortdf)
    ===============================================================================14
    对Series按照index排序，降序，重新设置index
    >>> idx = iris.index.tolist()
    >>> np.random.shuffle(idx)
    >>> iris.index = idx
    >>> sortdf = sort(iris["Sepal.Length"], by="index", isincreasing=0, isreindex=1)
    >>> print(sortdf)
    ===============================================================================15
    对Series按照index排序，降序，重新设置index，在原数据上修改
    >>> idx = iris.index.tolist()
    >>> np.random.shuffle(idx)
    >>> iris.index = idx
    >>> sortdf = sort(iris["Sepal.Length"], by="index", isincreasing=0, isreindex=1, isinplace=1)
    >>> print(sortdf)
    >>> print(iris)
    ===============================================================================16
    对Series按照value排序
    >>> sortdf = sort(iris["Sepal.Length"])
    >>> print(sortdf)
    ===============================================================================17
    对Series按照value排序，降序
    >>> sortdf = sort(iris["Sepal.Length"], isincreasing=0)
    >>> print(sortdf)
    ===============================================================================18
    对Series按照value排序，降序，重新设置索引
    >>> sortdf = sort(iris["Sepal.Length"], isincreasing=0, isreindex=1)
    >>> print(sortdf)
    ===============================================================================19
    对DataFrame的列名进行排序
    >>> sortdf = sort(iris, by="index", issortcol=1)
    >>> print(sortdf)
    ===============================================================================20
    """
    res = None
    if by == "index":
        if isinstance(df, pd.DataFrame):
            res = df.sort_index(
                ascending=bool(isincreasing),
                inplace=bool(isinplace),
                ignore_index=bool(isreindex),
                axis=issortcol)
        elif isinstance(df, pd.Series):
            res = df.sort_index(
                ascending=bool(isincreasing),
                inplace=bool(isinplace),
                ignore_index=bool(isreindex))
        else:
            pass
    else:
        if isinstance(df, pd.DataFrame):
            res = df.sort_values(by=by, ascending=bool(isincreasing) if isincreasing == 0 or isincreasing == 1 else list(
                map(lambda x: bool(x), isincreasing)), inplace=bool(isinplace), ignore_index=bool(isreindex))
        elif isinstance(df, pd.Series):
            res = df.sort_values(
                ascending=bool(isincreasing),
                inplace=bool(isinplace),
                ignore_index=bool(isreindex))
    return res
