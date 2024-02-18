import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def reshape(
    obj,
    convert_type="l2w",
    index=None,
    columns=None,
    values=None,
    groups=None
):
    """
    这是长宽数据转换的文档字符串。

    参数:
    obj (DataFrame): DataFrame对象。
    convert_type (str): 转换类型，长数据转为宽数据(long to wide)和宽数据转为长数据(wide to long){"l2w", "w2l"}。
    index (str or list of str): 控制长数据转为宽数据的参数，作为行名的列。
    columns (str or list of str): 控制长数据转为宽数据的参数，作为列名的列。
    values (str or list of str): 控制长数据转为宽数据的参数，作为DataFrame值的列。
    groups (dict): 控制宽数据转为长数据的参数，指定哪些列用于数据的column。


    示例:
    ===============================================================================0
    导入模块
    >>> import pandas as pd
    >>> with open("../reshape.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'], 'bar': ['A', 'B', 'C', 'A', 'B', 'C'], 'baz': [1, 2, 3, 4, 5, 6], 'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
    ===============================================================================1
    测试l2w
    >>> print(df)
    >>> res = reshape(df, "l2w", index='foo', columns='bar', values='baz')
    >>> print(res)
    ===============================================================================2
    测试w2l
    >>> res = reshape(df, "l2w", index='foo', columns='bar', values='baz')
    >>> print(res)
    >>> res = reshape(res, "w2l", groups={"baz": ["A", "B", "C"]})
    >>> print(res)
    ===============================================================================3
    """
    if convert_type == "l2w":
        res = pd.pivot(obj, index=index, columns=columns, values=values)
        return res
    elif convert_type == "w2l":
        res = pd.lreshape(obj, groups=groups)
        return res
    else:
        print("请输入正确的数据")
