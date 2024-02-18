from functools import partial
import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def numdesc(
        df,
        isprint=1):
    """
    这是一个对数值型单变量描述性分析的帮助文档。

    参数:
    df (DataFrame or Series): dataframe对象或者series对象。
    isprint (binary): 是否输出结果{1,0}。

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../numdesc.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx")
    ===============================================================================1
    DataFrame的测试
    >>> res = numdesc(iris.iloc[:, 1:-1], isprint=1)
    ===============================================================================2
    Series的测试
    >>> res = numdesc(iris["Petal.Length"], isprint=1)
    ===============================================================================3
    """
    res = None
    # 自定义函数
    q_10 = partial(pd.Series.quantile, q=0.10)
    q_20 = partial(pd.Series.quantile, q=0.20)
    q_25 = partial(pd.Series.quantile, q=0.25)
    q_30 = partial(pd.Series.quantile, q=0.30)
    q_40 = partial(pd.Series.quantile, q=0.40)
    q_60 = partial(pd.Series.quantile, q=0.60)
    q_70 = partial(pd.Series.quantile, q=0.70)
    q_75 = partial(pd.Series.quantile, q=0.75)
    q_80 = partial(pd.Series.quantile, q=0.80)
    q_90 = partial(pd.Series.quantile, q=0.90)
    sum_duplicate = partial(lambda x: x.duplicated().sum())
    sum_unique = partial(lambda x: x.unique().size)
    sum_na = partial(lambda x: x.isna().sum())
    # 给函数一个名称
    q_10.__name__ = "10%"
    q_20.__name__ = "20%"
    q_25.__name__ = "25%"
    q_30.__name__ = "30%"
    q_40.__name__ = "40%"
    q_60.__name__ = "60%"
    q_70.__name__ = "70%"
    q_75.__name__ = "75%"
    q_80.__name__ = "80%"
    q_90.__name__ = "90%"
    sum_duplicate.__name__ = "duplicate_num"
    sum_unique.__name__ = "unique_num"
    sum_na.__name__ = "na_num"
    res = df.agg(["sum",
                  "count",
                  "mean",
                  "std",
                  "var",
                  "min",
                  q_25,
                  "median",
                  q_75,
                  "max",
                  sum_duplicate,
                  sum_unique,
                  sum_na,
                  "kurtosis",
                  "skew",
                  q_10,
                  q_20,
                  q_30,
                  q_40,
                  q_60,
                  q_70,
                  q_80,
                  q_90])
    # 输出统计量结果
    if bool(isprint):
        print(res)
    else:
        pass
    return res
