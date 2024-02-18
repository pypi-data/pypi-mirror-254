import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def apply(
    obj,
    func=None,
    applytowhat="obj",
    axis=0,
    **kwargs
):
    """
    这是函数应用到数据上的文档字符串。

    参数:
    obj (Series or DataFrame): Series对象或者是DataFrame对象。
    applytowhat (str): 将函数应用到什么对象{"element", "obj"}。
    1. element表示对Series的每一个元素进行操作。
    2. obj表示对整个Series或者DataFrame进行操作。
    axis (binary): 按照某个轴进行应用函数{1,0}。
    func (str or callalbe or dict or list): 应用的函数。
    str可以的取值有{
        "any",
        "all",
        "count",
        "cov",
        "idxmax",
        "idxmin",
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
        "head",
        "tail"
    }

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../apply.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx")
    >>> sepal_length = iris["Sepal.Length"]
    ===============================================================================1
    测试Series参数，applytowhat为obj，func为str=any
    >>> res = apply(sepal_length, "any")
    >>> print(res)
    ===============================================================================2
    测试Series参数，applytowhat为obj，func为str=all
    >>> res = apply(sepal_length, "all")
    >>> print(res)
    ===============================================================================3
    测试Series参数，applytowhat为obj，func为str=count
    >>> res = apply(sepal_length, "count")
    >>> print(res)
    ===============================================================================4
    测试Series参数，applytowhat为obj，func为str=idxmax
    >>> res = apply(sepal_length, "idxmax")
    >>> print(res)
    ===============================================================================5
    测试Series参数，applytowhat为obj，func为str=idxmin
    >>> res = apply(sepal_length, "idxmin")
    >>> print(res)
    ===============================================================================6
    测试Series参数，applytowhat为obj，func为str=max
    >>> res = apply(sepal_length, "max")
    >>> print(res)
    ===============================================================================7
    测试Series参数，applytowhat为obj，func为str=min
    >>> res = apply(sepal_length, "min")
    >>> print(res)
    ===============================================================================8
    测试Series参数，applytowhat为obj，func为str=mean
    >>> res = apply(sepal_length, "mean")
    >>> print(res)
    ===============================================================================9
    测试Series参数，applytowhat为obj，func为str=median
    >>> res = apply(sepal_length, "median")
    >>> print(res)
    ===============================================================================10
    测试Series参数，applytowhat为obj，func为str=sum
    >>> res = apply(sepal_length, "sum")
    >>> print(res)
    ===============================================================================11
    测试Series参数，applytowhat为obj，func为str=nunique
    >>> res = apply(sepal_length, "unique")
    >>> print(res)
    ===============================================================================12
    测试Series参数，applytowhat为obj，func为str=prod
    >>> res = apply(sepal_length, "prod")
    >>> print(res)
    ===============================================================================13
    测试Series参数，applytowhat为obj，func为str=quantile
    >>> res = apply(sepal_length, "quantile", q=0.9)
    >>> print(res)
    ===============================================================================14
    测试Series参数，applytowhat为obj，func为str=sem
    >>> res = apply(sepal_length, "sem")
    >>> print(res)
    ===============================================================================15
    测试Series参数，applytowhat为obj，func为str=size
    >>> res = apply(sepal_length, "size")
    >>> print(res)
    ===============================================================================16
    测试Series参数，applytowhat为obj，func为str=skew
    >>> res = apply(sepal_length, "skew")
    >>> print(res)
    ===============================================================================17
    测试Series参数，applytowhat为obj，func为str=std
    >>> res = apply(sepal_length, "std")
    >>> print(res)
    ===============================================================================18
    测试Series参数，applytowhat为obj，func为str=var
    >>> res = apply(sepal_length, "var")
    >>> print(res)
    ===============================================================================19
    测试Series参数，applytowhat为obj，func为str=bfill
    >>> res = apply(sepal_length, "bfill")
    >>> print(res)
    ===============================================================================20
    测试Series参数，applytowhat为obj，func为str=cumsum
    >>> res = apply(sepal_length, "cumsum")
    >>> print(res)
    ===============================================================================21
    测试Series参数，applytowhat为obj，func为str=cumprod
    >>> res = apply(sepal_length, "cumprod")
    >>> print(res)
    ===============================================================================22
    测试Series参数，applytowhat为obj，func为str=cummax
    >>> res = apply(sepal_length, "cummax")
    >>> print(res)
    ===============================================================================23
    测试Series参数，applytowhat为obj，func为str=cummin
    >>> res = apply(sepal_length, "cummin")
    >>> print(res)
    ===============================================================================24
    测试Series参数，applytowhat为obj，func为str=diff
    >>> res = apply(sepal_length, "diff")
    >>> print(res)
    ===============================================================================25
    测试Series参数，applytowhat为obj，func为str=ffill
    >>> res = apply(sepal_length, "ffill")
    >>> print(res)
    ===============================================================================26
    测试Series参数，applytowhat为obj，func为str=fillna
    >>> res = apply(sepal_length, "fillna", value=100)
    >>> print(res)
    ===============================================================================27
    测试Series参数，applytowhat为obj，func为str=rank
    >>> res = apply(sepal_length, "rank")
    >>> print(res)
    ===============================================================================28
    测试Series参数，applytowhat为obj，func为str=shift
    >>> res = apply(sepal_length, "shift", periods=1)
    >>> print(res)
    ===============================================================================29
    测试Series参数，applytowhat为obj，func为str=head
    >>> res = apply(sepal_length, "head")
    >>> print(res)
    ===============================================================================30
    测试Series参数，applytowhat为obj，func为str=tail
    >>> res = apply(sepal_length, "tail")
    >>> print(res)
    ===============================================================================31
    测试Series参数，applytowhat为element，func为lambda x: str(x).split(".")[1]
    >>> res = apply(sepal_length, lambda x: str(x).split(".")[1], applytowhat="element")
    >>> print(res)
    ===============================================================================32
    测试DataFrame参数，func为str=any
    >>> res = apply(iris, "any")
    >>> print(res)
    ===============================================================================33
    测试DataFrame参数，func为str=all
    >>> res = apply(iris, "all")
    >>> print(res)
    ===============================================================================34
    测试DataFrame参数，func为str=count
    >>> res = apply(iris, "count")
    >>> print(res)
    ===============================================================================35
    测试DataFrame参数，func为str=idxmax
    >>> res = apply(iris, "idxmax")
    >>> print(res)
    ===============================================================================36
    测试DataFrame参数，func为str=idxmin
    >>> res = apply(iris, "idxmin")
    >>> print(res)
    ===============================================================================37
    测试DataFrame参数，func为str=max
    >>> res = apply(iris, "max")
    >>> print(res)
    ===============================================================================38
    测试DataFrame参数，func为str=min
    >>> res = apply(iris, "min")
    >>> print(res)
    ===============================================================================39
    测试DataFrame参数，func为str=mean
    >>> res = apply(iris.iloc[:,:-1], "mean")
    >>> print(res)
    ===============================================================================40
    测试DataFrame参数，func为str=median
    >>> res = apply(iris.iloc[:,:-1], "median")
    >>> print(res)
    ===============================================================================41
    测试DataFrame参数，func为str=sum
    >>> res = apply(iris.iloc[:,:-1], "sum")
    >>> print(res)
    ===============================================================================42
    测试DataFrame参数，func为str=prod
    >>> res = apply(iris.iloc[:,:-1], "prod")
    >>> print(res)
    ===============================================================================43
    测试DataFrame参数，func为str=quantile
    >>> res = apply(iris.iloc[:,:-1], "quantile", q=0.9)
    >>> print(res)
    ===============================================================================44
    测试DataFrame参数，func为str=sem
    >>> res = apply(iris.iloc[:,:-1], "sem")
    >>> print(res)
    ===============================================================================45
    测试DataFrame参数，func为str=size
    >>> res = apply(iris.iloc[:,:-1], "size")
    >>> print(res)
    ===============================================================================46
    测试DataFrame参数，func为str=skew
    >>> res = apply(iris.iloc[:,:-1], "skew")
    >>> print(res)
    ===============================================================================47
    测试DataFrame参数，func为str=std
    >>> res = apply(iris.iloc[:,:-1], "std")
    >>> print(res)
    ===============================================================================48
    测试DataFrame参数，func为str=var
    >>> res = apply(iris.iloc[:,:-1], "var")
    >>> print(res)
    ===============================================================================49
    测试DataFrame参数，func为str=bfill
    >>> res = apply(iris.iloc[:,:-1], "bfill")
    >>> print(res)
    ===============================================================================50
    测试DataFrame参数，func为str=cumsum
    >>> res = apply(iris.iloc[:,:-1], "cumsum")
    >>> print(res)
    ===============================================================================51
    测试DataFrame参数，func为str=cumprod
    >>> res = apply(iris.iloc[:,:-1], "cumprod")
    >>> print(res)
    ===============================================================================52
    测试DataFrame参数，func为str=cummax
    >>> res = apply(iris.iloc[:,:-1], "cummax")
    >>> print(res)
    ===============================================================================53
    测试DataFrame参数，func为str=cummin
    >>> res = apply(iris.iloc[:,:-1], "cummin", axis=1)
    >>> print(res)
    ===============================================================================54
    测试DataFrame参数，func为str=diff
    >>> res = apply(iris.iloc[:,:-1], "diff", axis=1)
    >>> print(res)
    ===============================================================================55
    测试DataFrame参数，func为str=ffill
    >>> res = apply(iris.iloc[:,:-1], "ffill")
    >>> print(res)
    ===============================================================================56
    测试DataFrame参数，func为str=fillna
    >>> res = apply(iris.iloc[:,:-1], "fillna", value=100)
    >>> print(res)
    ===============================================================================57
    测试DataFrame参数，func为str=rank
    >>> res = apply(iris.iloc[:,:-1], "rank")
    >>> print(res)
    ===============================================================================58
    测试DataFrame参数，func为str=shift
    >>> res = apply(iris.iloc[:,:-1], "shift", periods=1)
    >>> print(res)
    ===============================================================================59
    测试DataFrame参数，func为str=head
    >>> res = apply(iris.iloc[:,:-1], "head")
    >>> print(res)
    ===============================================================================60
    测试DataFrame参数，func为str=tail
    >>> res = apply(iris.iloc[:,:-1], "tail")
    >>> print(res)
    ===============================================================================61
    测试DataFrame参数，func为str=tail
    >>> res = apply(iris.iloc[:,:-1], "tail")
    >>> print(res)
    ===============================================================================62
    测试DataFrame参数，func为自定义函数
    >>> res = apply(iris.iloc[:,:-1], lambda x: x+1)
    >>> print(res)
    ===============================================================================63
    测试Series参数，func为列表，非聚合函数
    >>> res = apply(sepal_length, ["cumsum", lambda x: x+1])
    >>> print(res)
    ===============================================================================64
    测试Series参数，func为列表，聚合函数
    >>> res = apply(sepal_length, ["max", lambda x: x.max()-x.min()])
    >>> print(res)
    ===============================================================================65
    测试DataFrame参数，func为字典，非聚合函数
    >>> res = apply(iris.iloc[:, :-1], {"Sepal.Width": "cumsum", "Sepal.Length": lambda x: x+1})
    >>> print(res)
    ===============================================================================66
    测试DataFrame参数，func为字典，聚合函数
    >>> res = apply(iris.iloc[:, :-1], {"Sepal.Width": "sum", "Sepal.Length": lambda x: x.max()-x.min()})
    >>> print(res)
    ===============================================================================67
    测试DataFrame参数，func为列表，非聚合函数
    >>> res = apply(iris.iloc[:, :-1], ["cumsum", lambda x: x+1])
    >>> print(res)
    ===============================================================================68
    测试DataFrame参数，func为列表，聚合函数
    >>> res = apply(iris.iloc[:, :-1], ["sum", lambda x: x.max()-x.min()])
    >>> print(res)
    ===============================================================================69
    """
    if isinstance(obj, pd.Series):
        if applytowhat == "obj":
            if isinstance(func, list):
                try:
                    res = obj.transform(func, **kwargs)
                except BaseException:
                    res = obj.agg(func, **kwargs)
            else:
                res = obj.apply(func, **kwargs)
        elif applytowhat == "element":
            res = obj.map(func, **kwargs)
        return res
    elif isinstance(obj, pd.DataFrame):
        if applytowhat == "obj":
            if isinstance(func, list) or isinstance(func, dict):
                try:
                    res = obj.transform(func, axis=axis, **kwargs)
                except BaseException:
                    res = obj.agg(func, **kwargs)
            else:
                res = obj.apply(func, axis=axis, **kwargs)
        else:
            res = obj.apply(func, **kwargs)
        return res
    else:
        print("请输入正确的数据")
