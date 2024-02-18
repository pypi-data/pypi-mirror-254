import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def freq(
    obj,
    normalize=0,
    sort=1,
    ascending=0,
    dropna=1,
    bins=None,
    subset=None
):
    """
    这是频数统计的文档字符串。

    参数:
    obj (Series or DataFrame): Series对象或者DataFrame对象。
    normalize (binary): 是否显示频率{1,0}。
    sort (binary): 是否对频数统计结果进行排序{1,0}。
    ascending (binary): 是否升序排列{1,0}。
    dropna (binary): 是否删除缺失值{1,0}。
    bins (int): 对Series数据进行等距分组后，对分组标签进行频数统计时的等距分组的组数。
    subset (list of str or str): DataFrame对象进行频数统计的列。

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../freq.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx")
    >>> toothgrowth = read("../data/toothgrowth.txt", textfileparamsdict={"sep": "\t"})
    ===============================================================================1
    测试DataFrame对象
    >>> res = freq(toothgrowth)
    >>> print(res)
    ===============================================================================2
    测试DataFrame对象，频率统计
    >>> res = freq(toothgrowth, normalize=1)
    >>> print(res)
    ===============================================================================3
    测试DataFrame对象，不排序
    >>> res = freq(toothgrowth, sort=0)
    >>> print(res)
    ===============================================================================4
    测试DataFrame对象，升序排列
    >>> res = freq(toothgrowth, ascending=1)
    >>> print(res)
    ===============================================================================5
    测试DataFrame对象，指定列
    >>> res = freq(toothgrowth, subset="supp")
    >>> print(res)
    ===============================================================================6
    测试Series对象
    >>> res = freq(iris["Species"])
    >>> print(res)
    ===============================================================================7
    测试Series对象，频率统计
    >>> res = freq(iris["Sepal.Length"], normalize=1)
    >>> print(res)
    ===============================================================================8
    测试Series对象，不排序
    >>> res = freq(iris["Sepal.Length"], sort=0)
    >>> print(res)
    ===============================================================================9
    测试Series对象，升序排列
    >>> res = freq(iris["Sepal.Length"], ascending=1)
    >>> print(res)
    ===============================================================================10
    测试Series对象，等距分组为5组
    >>> res = freq(iris["Sepal.Length"], ascending=1, bins=5)
    >>> print(res)
    ===============================================================================11
    """
    if isinstance(obj, pd.DataFrame):
        res = obj.value_counts(
            normalize=bool(normalize),
            sort=bool(sort),
            ascending=bool(ascending),
            dropna=bool(dropna),
            subset=subset)
        return res
    elif isinstance(obj, pd.Series):
        res = obj.value_counts(
            normalize=bool(normalize),
            sort=bool(sort),
            ascending=bool(ascending),
            dropna=bool(dropna),
            bins=bins)
        return res
    else:
        print("请输入正确的数据")
