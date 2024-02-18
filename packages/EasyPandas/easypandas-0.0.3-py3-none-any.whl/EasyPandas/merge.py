import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def merge(
    obj=None,
    axis=0,
    keys=None,
    ignore_index=0,
    join="inner",
    isbyvar=0,
    how="inner",
    on=None
):
    """
    这是一个合并数据的文档字符串。

    参数:
    obj (list of DataFrame or tuple of DataFrame): dataframe对象构成的列表或者元组。
    axis (binary): 按行合并还是按列合并{1,0}。
    keys (list of str): 对合并后的数据创建多层索引中的第一级索引。
    ignore_index (binary): 对合并后的数据是否重新对索引编号{1,0}。
    join (str): 合并方式{"inner", "outer"}。
    isbyvar (binary): 是否按照某个共同变量来合并数据{1,0}。
    how (str): 按照某个共同变量合并数据的方法{"left", "right", "outer", "inner", "cross"}。
    on (str or list of str): 按照哪个共同变量合并数据。

    示例:
    ===============================================================================0
    导入模块
    >>> import pandas as pd
    >>> with open("../merge.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> df1 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'], 'value_1': [1, 2, 3, 5]})
    >>> df2 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'], 'value_2': [5, 6, 7, 8]})
    ===============================================================================1
    测试按照变量合并，inner合并
    >>> print(df1)
    >>> print(df2)
    >>> res = merge([df1, df2], isbyvar=1, on="key", how="inner")
    >>> print(res)
    ===============================================================================2
    测试按照变量合并，outer合并
    >>> print(df1)
    >>> print(df2)
    >>> res = merge([df1, df2], isbyvar=1, on="key", how="outer")
    >>> print(res)
    ===============================================================================3
    测试按照变量合并，left合并
    >>> print(df1)
    >>> print(df2)
    >>> res = merge([df1, df2], isbyvar=1, on="key", how="left")
    >>> print(res)
    ===============================================================================4
    测试普通合并，按行合并
    >>> print(df1)
    >>> print(df2)
    >>> res = merge([df1, df2])
    >>> print(res)
    ===============================================================================5
    测试普通合并，按列合并
    >>> print(df1)
    >>> print(df2)
    >>> res = merge([df1, df2], axis=1)
    >>> print(res)
    ===============================================================================6
    测试普通合并，按列合并，重新排列索引
    >>> print(df1)
    >>> print(df2)
    >>> res = merge([df1, df2], axis=1, ignore_index=1)
    >>> print(res)
    ===============================================================================7
    测试普通合并，按行合并，设置多重索引
    >>> print(df1)
    >>> print(df2)
    >>> res = merge([df1, df2], axis=0, keys=["left", "right"])
    >>> print(res)
    ===============================================================================8
    测试普通合并，按行合并，outer合并
    >>> print(df1)
    >>> print(df2)
    >>> res = merge([df1, df2], axis=0, keys=["left", "right"], join="outer")
    >>> print(res)
    ===============================================================================9
    """
    if not bool(isbyvar):
        res = pd.concat(
            obj,
            axis=axis,
            ignore_index=ignore_index,
            keys=keys,
            join=join)
        return res
    elif bool(isbyvar):
        res = pd.merge(obj[0], obj[1], on=on, how=how)
        return res
    else:
        print("合并数据失败！")
