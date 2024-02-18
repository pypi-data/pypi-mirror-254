import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def index(
    obj,
    index=None,
    columns=None,
    indexgdata=0,
    columngdata=0,
    drop=0,
    reset=0
):
    """
    这是修改行名列名的文档字符串。

    参数:
    obj (Series or DataFrame): Series对象或者DataFrame对象。
    index (list of str or str or dict): 要修改的行名或者是要将某列作为index。
    columns (list of str or dict): 要修改的列名。
    indexgdata (binary): 修改index是否要影响原始数据。
    columngdata (binary): 修改column是否要影响原始数据。
    drop (binary): 当将数据中的某列作为index时，是否需要删除原数据中那一列。
    reset (binary): 是否将index转为数据中的列。


    示例:
    ===============================================================================0
    导入模块
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../index.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx")
    >>> sepal_length = iris["Sepal.Length"]
    ===============================================================================1
    测试Series参数
    >>> res = index(sepal_length, index=[i**2 for i in range(150)])
    >>> print(res)
    ===============================================================================2
    测试Series参数，修改原始数据
    >>> res = index(sepal_length, index=[i**2 for i in range(150)], indexgdata=1)
    >>> print(res)
    ===============================================================================3
    测试Series参数，将index转为一列
    >>> res = index(sepal_length)
    >>> print(res)
    ===============================================================================4
    测试DataFrame参数，修改行名
    >>> res = index(iris, index=[i**2 for i in range(150)])
    >>> print(res)
    ===============================================================================5
    测试DataFrame参数，原数据修改
    >>> res = index(iris, index=[i**2 for i in range(150)], indexgdata=1)
    >>> print(res)
    ===============================================================================6
    测试DataFrame参数，修改列名
    >>> res = index(iris, columns=iris.columns.tolist()[:-1] + ["A"])
    >>> print(res)
    ===============================================================================7
    测试DataFrame参数，修改列名，原数据修改
    >>> res = index(iris, columns=iris.columns.tolist()[:-1] + ["A"], columngdata=1)
    >>> print(res)
    ===============================================================================8
    测试DataFrame参数，修改列名和列名
    >>> res = index(iris, columns=iris.columns.tolist()[:-1] + ["A"], index=[i**2 for i in range(150)])
    >>> print(res)
    ===============================================================================9
    测试DataFrame参数，修改列名和列名，原数据修改
    >>> res = index(iris, columns=iris.columns.tolist()[:-1] + ["A"], index=[i**2 for i in range(150)], indexgdata=1, columngdata=1)
    >>> print(res)
    ===============================================================================10
    测试DataFrame参数，将某列作为行名
    >>> res = index(iris, index="Sepal.Length")
    >>> print(res)
    ===============================================================================11
    测试DataFrame参数，将某列作为行名，从原数据中删除那一列
    >>> res = index(iris, index="Sepal.Length", drop=1)
    >>> print(res)
    ===============================================================================12
    测试DataFrame参数，将index转为列数据
    >>> res = index(iris, reset=1)
    >>> print(res)
    ===============================================================================13
    """
    if isinstance(obj, pd.Series):
        if isinstance(index, list):
            if bool(indexgdata):
                res = obj.reindex(index=index)
            else:
                res = obj.copy()
                res.index = index
        else:
            res = obj.reset_index()
        return res
    elif isinstance(obj, pd.DataFrame):
        if isinstance(index, list) or isinstance(columns, list):
            if bool(indexgdata) and bool(columngdata):
                res = obj.reindex(index=index, columns=columns)
            elif bool(indexgdata) and not bool(columngdata):
                res = obj.reindex(index=index, columns=None)
                res.columns = columns if columns is not None else obj.columns
            elif not bool(indexgdata) and bool(columngdata):
                res = obj.reindex(index=None, columns=columns)
                res.index = index if index is not None else obj.index
            else:
                res = obj.copy()
                res.index = index if index is not None else obj.index
                res.columns = columns if columns is not None else obj.columns
        else:
            if not bool(reset):
                res = obj.set_index(index, drop=bool(drop))
            else:
                res = obj.reset_index()
        return res
