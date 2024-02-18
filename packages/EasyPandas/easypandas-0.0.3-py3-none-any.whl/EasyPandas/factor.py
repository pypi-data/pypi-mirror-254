import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def factor(
    obj,
    as_category=0
):
    """
    这是将字符数据转为离散型数值数据的文档字符串。

    参数:
    obj (Series): Series对象。
    as_category (binary): 是否转为分类变量{1,0}。

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../factor.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> df = read("../data/toothgrowth.txt", textfileparamsdict={"sep": "\t"})
    ===============================================================================1
    基本测试
    >>> res = factor(df["supp"])
    >>> print(res)
    ===============================================================================2
    """
    if not bool(as_category):
        value, category = pd.factorize(obj)
        res = pd.Series(value)
        info_dict = {"discrete_value": res.unique().tolist(), "category": category.tolist()}
        print("字符串数据的类别和离散化值对应关系如下", info_dict, sep="\n")
        return res
    else:
        value, category = pd.factorize(obj)
        res = pd.Categorical(obj, categories=category)
        return res
