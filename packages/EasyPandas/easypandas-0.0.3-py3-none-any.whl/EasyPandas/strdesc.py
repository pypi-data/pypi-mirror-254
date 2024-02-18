from functools import partial
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def strdesc(df, isprint=1):
    """
    这是一个对字符型单变量描述性分析的帮助文档。

    df (DataFrame or Series): dataframe对象或者series对象。
    isprint (binary): 是否输出结果{1,0}。

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../strdesc.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> auto = read("../data/auto.dta")
    ===============================================================================1
    DataFrame的测试
    >>> res = strdesc(auto[["make", "foreign"]], isprint=1)
    ===============================================================================2
    Series的测试
    >>> res = strdesc(auto["foreign"], isprint=1)
    ===============================================================================3
    """
    res = None
    # 自定义函数
    sum_unique = partial(lambda x: x.unique().size)
    sum_duplicate = partial(lambda x: x.duplicated().sum())
    sum_na = partial(lambda x: x.isna().sum())
    max_freq = partial(lambda x: x.value_counts().max())
    min_freq = partial(lambda x: x.value_counts().min())
    # 给函数一个名称
    sum_unique.__name__ = "unique_num"
    sum_duplicate.__name__ = "duplicate_num"
    sum_na.__name__ = "na_num"
    max_freq.__name__ = "max_freq"
    min_freq.__name__ = "min_freq"
    res = df.agg(["count", sum_duplicate, sum_unique,
                 sum_na, max_freq, min_freq])
    # 输出统计量结果
    if bool(isprint):
        print(res)
    else:
        pass
    return res
