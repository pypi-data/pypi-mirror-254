import numpy as np
import pandas as pd


def filter(df, condition1=None, condition2=None, condition_relation=None):
    """
    这是一个筛选数据的帮助文档。

    参数:
    df (DataFrame or Series): DataFrame对象或者Series对象。
    condition1 (str): 筛选条件。
    condition2 (str): 筛选条件。
    condition_relation (str): 多个条件之间的关系{"and", "or"}。
    筛选条件的格式如下：
    1. 数据的列名必须用反引号``包裹起来。
    2. 数值变量比较运算符有：>(大于),>=(大于等于),<(小于),<=(小于等于),==(等于),!=(不等于)
    3. 字符变量比较运算符有：==(等于),(!=)(不等于),^^(开头是),$$(结尾是),^C$(包含),!^C$(不包含),in [](在某个列表中), not in [](不在某个列表中)
    4. 数据各个列之间的比较：`a`>`b`(a列大于b列),`a`>=`b`(a列大于等于b列)`a`==`b`(a列等于b列),`a`!=`b`(a列不等于b列),`a`<`b`(a列小于b列),`a`<=`b`(a列小于等于b列)

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../filter.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx")
    ===============================================================================1
    DataFrame的筛选
    ===============================================================================2
    等于筛选
    >>> res = filter(iris, "`Sepal.Length` == 4.9")
    >>> print(res)
    ===============================================================================3
    不等于筛选
    >>> res = filter(iris, "`Sepal.Length` != 4.9")
    >>> print(res)
    ===============================================================================4
    大于筛选
    >>> res = filter(iris, "`Sepal.Length` > 4.9")
    >>> print(res)
    ===============================================================================5
    大于等于筛选
    >>> res = filter(iris, "`Sepal.Length` >= 4.9")
    >>> print(res)
    ===============================================================================6
    小于筛选
    >>> res = filter(iris, "`Sepal.Length` < 4.9")
    >>> print(res)
    ===============================================================================7
    小于等于筛选
    >>> res = filter(iris, "`Sepal.Length` <= 4.9")
    >>> print(res)
    ===============================================================================8
    字符串等于筛选
    >>> res = filter(iris, "`Species` == 'setosa'")
    >>> print(res)
    ===============================================================================9
    字符串不等于筛选
    >>> res = filter(iris, "`Species` != 'setosa'")
    >>> print(res)
    ===============================================================================10
    字符串包含筛选
    >>> res = filter(iris, "`Species` ^C$ 'v'")
    >>> print(res)
    ===============================================================================11
    字符串不包含筛选
    >>> res = filter(iris, "`Species` !^C$ 'v'")
    >>> print(res)
    ===============================================================================12
    字符串开始为
    >>> res = filter(iris, "`Species` ^^ 'set'")
    >>> print(res)
    ===============================================================================13
    字符串结束为
    >>> res = filter(iris, "`Species` $$ 'color'")
    >>> print(res)
    ===============================================================================14
    列之间的大于比较
    >>> res = filter(iris, "`Sepal.Length` > `Petal.Length`")
    >>> print(res)
    ===============================================================================15
    列之间的大于等于比较
    >>> res = filter(iris, "`Sepal.Width` > `Petal.Width`")
    >>> print(res)
    ===============================================================================16
    列之间的小于比较
    >>> res = filter(iris, "`Sepal.Width` < `Petal.Width`")
    >>> print(res)
    ===============================================================================17
    列之间的小于等于比较
    >>> res = filter(iris, "`Sepal.Length` <= `Petal.Length`")
    >>> print(res)
    ===============================================================================18
    列之间的等于比较
    >>> res = filter(iris, "`Sepal.Length` == `Petal.Length`")
    >>> print(res)
    ===============================================================================19
    列之间的不等于比较
    >>> res = filter(iris, "`Sepal.Width` != `Petal.Width`")
    >>> print(res)
    ===============================================================================20
    多个筛选条件
    >>> res = filter(iris, "`Sepal.Length` >= 5", "`Sepal.Length` <= 4.5", "and")
    >>> print(res)
    >>> res = filter(iris, "`Sepal.Length` >= 5", "`Sepal.Length` <= 4.5", "or")
    >>> print(res)
    >>> res = filter(iris, "`Sepal.Length` >= 5", "`Sepal.Length` <= 4.5", None)
    >>> print(res)
    >>> res = filter(iris, "`Species` ^C$ 'color'", "`Species` ^C$ 'set'", "or")
    >>> print(res)
    >>> res = filter(iris, "`Species` ^C$ 'color'", "`Sepal.Length` > 5", "and")
    >>> print(res)
    ===============================================================================21
    测试Series
    ===============================================================================22
    等于筛选
    >>> res = filter(iris["Sepal.Length"], "== 4.9")
    >>> print(res)
    ===============================================================================23
    不等于筛选
    >>> res = filter(iris["Sepal.Length"], "!= 4.9")
    >>> print(res)
    ===============================================================================24
    大于筛选
    >>> res = filter(iris["Sepal.Length"], "> 4.9")
    >>> print(res)
    ===============================================================================25
    大于等于筛选
    >>> res = filter(iris["Sepal.Length"], ">= 4.9")
    >>> print(res)
    ===============================================================================26
    小于筛选
    >>> res = filter(iris["Sepal.Length"], "< 4.9")
    >>> print(res)
    ===============================================================================27
    小于等于筛选
    >>> res = filter(iris["Sepal.Length"], "<= 4.9")
    >>> print(res)
    ===============================================================================28
    字符串等于筛选
    >>> res = filter(iris["Species"], "== 'setosa'")
    >>> print(res)
    ===============================================================================29
    字符串不等于筛选
    >>> res = filter(iris["Species"], "!='setosa'")
    >>> print(res)
    ===============================================================================30
    字符串包含筛选
    >>> res = filter(iris["Species"], "^C$ 'v'")
    >>> print(res)
    ===============================================================================31
    字符串不包含筛选
    >>> res = filter(iris["Species"], "!^C$ 'v'")
    >>> print(res)
    ===============================================================================32
    字符串开始为
    >>> res = filter(iris["Species"], "^^ 'set'")
    >>> print(res)
    ===============================================================================33
    字符串结束为
    >>> res = filter(iris["Species"], "$$ 'color'")
    >>> print(res)
    ===============================================================================34
    对于一个一般的Series
    ===============================================================================35
    >>> s = pd.Series([i for i in range(100)])
    >>> res = filter(s, ">90")
    >>> print(res)
    ===============================================================================36
    >>> s = pd.Series([i for i in range(100)])
    >>> res = filter(s, "in [90, 99]")
    >>> print(res)
    ===============================================================================37
    >>> s = pd.Series([i for i in range(100)])
    >>> res = filter(s, "not in [90, 99]")
    >>> print(res)
    ===============================================================================38
    """
    res = None
    if isinstance(df, pd.DataFrame):
        if condition1 is None and condition2 is None:
            res = df.head()
            return res
        elif condition1 is not None and condition2 is None:
            if condition1.__contains__("^^"):
                condition1_lst = condition1.replace(" ", "").split("^^")
                res = df[df[condition1_lst[0].replace("`", "")].str.startswith(
                    condition1_lst[1].replace("'", ""))]
            elif condition1.__contains__("$$"):
                condition1_lst = condition1.replace(" ", "").split("$$")
                res = df[df[condition1_lst[0].replace("`", "")].str.endswith(
                    condition1_lst[1].replace("'", ""))]
            elif condition1.__contains__("!^C$"):
                condition1_lst = condition1.replace(" ", "").split("!^C$")
                res = df[~df[condition1_lst[0].replace("`", "")].str.contains(
                    condition1_lst[1].replace("'", ""))]
            elif condition1.__contains__("^C$"):
                condition1_lst = condition1.replace(" ", "").split("^C$")
                res = df[df[condition1_lst[0].replace("`", "")].str.contains(
                    condition1_lst[1].replace("'", ""))]
            else:
                res = df.query(condition1)
            return res
        elif condition1 is not None and condition2 is not None:
            if condition1.__contains__("^^"):
                condition1_lst = condition1.replace(" ", "").split("^^")
                res1 = df[df[condition1_lst[0].replace("`", "")].str.startswith(
                    condition1_lst[1].replace("'", ""))]
            elif condition1.__contains__("$$"):
                condition1_lst = condition1.replace(" ", "").split("$$")
                res1 = df[df[condition1_lst[0].replace("`", "")].str.endswith(
                    condition1_lst[1].replace("'", ""))]
            elif condition1.__contains__("!^C$"):
                condition1_lst = condition1.replace(" ", "").split("!^C$")
                res1 = df[~df[condition1_lst[0].replace("`", "")].str.contains(
                    condition1_lst[1].replace("'", ""))]
            elif condition1.__contains__("^C$"):
                condition1_lst = condition1.replace(" ", "").split("^C$")
                res1 = df[df[condition1_lst[0].replace("`", "")].str.contains(
                    condition1_lst[1].replace("'", ""))]
            else:
                res1 = df.query(condition1)
            if condition2.__contains__("^^"):
                condition2_lst = condition2.replace(" ", "").split("^^")
                res2 = df[df[condition2_lst[0].replace("`", "")].str.startswith(
                    condition2_lst[1].replace("'", ""))]
            elif condition2.__contains__("$$"):
                condition2_lst = condition2.replace(" ", "").split("$$")
                res2 = df[df[condition2_lst[0].replace("`", "")].str.endswith(
                    condition2_lst[1].replace("'", ""))]
            elif condition2.__contains__("!^C$"):
                condition2_lst = condition2.replace(" ", "").split("!^C$")
                res2 = df[~df[condition2_lst[0].replace("`", "")].str.contains(
                    condition2_lst[1].replace("'", ""))]
            elif condition2.__contains__("^C$"):
                condition2_lst = condition2.replace(" ", "").split("^C$")
                res2 = df[df[condition2_lst[0].replace("`", "")].str.contains(
                    condition2_lst[1].replace("'", ""))]
            else:
                res2 = df.query(condition2)
            if condition_relation == "and":
                res = df.loc[np.intersect1d(
                    np.array(res1.index), np.array(res2.index))]
            elif condition_relation == "or":
                res = df.loc[np.union1d(
                    np.array(res1.index), np.array(res2.index))]
            else:
                print("请给出条件之间的关系！")
            return res
        else:
            return res
    elif isinstance(df, pd.Series):
        if condition1 is not None:
            condition1 = "`" + \
                (df.name if df.name is not None else "Name") + "` " + condition1
        if condition2 is not None:
            condition2 = "`" + \
                (df.name if df.name is not None else "Name") + "` " + condition2
        newdf = pd.DataFrame(df) if df.name is not None else pd.DataFrame(
            df, columns=["Name"])
        res = filter(newdf, condition1, condition2, condition_relation)
        return res.iloc[:, 0]
    else:
        return res
